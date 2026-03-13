#!/usr/bin/env python3
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA_VERSION = "5.0"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    if not path.exists() or path.stat().st_size == 0:
        return ""
    return sha256_text(path.read_text(encoding="utf-8", errors="replace"))


def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path):
    if not path.exists() or path.stat().st_size == 0:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def contains(path: Path, needle: str) -> bool:
    return needle in read_text(path)


def json_contains(obj, needle: str) -> bool:
    try:
        return needle in json.dumps(obj, ensure_ascii=False)
    except Exception:
        return False


def main() -> int:
    student_token = os.getenv("STUDENT_TOKEN", "").strip()
    student_name = os.getenv("STUDENT_NAME", "").strip()
    student_group = os.getenv("STUDENT_GROUP", "").strip()

    if not student_token or not student_name or not student_group:
        print("ERROR: set STUDENT_TOKEN, STUDENT_NAME, STUDENT_GROUP", file=sys.stderr)
        return 3

    th8 = token_hash8(student_token)

    # Paths
    p_yang = ART / "yang" / "pyang_tree.txt"

    p_webex_room = ART / "webex" / "room_create.json"

    p_pt_ext = ART / "pt" / "external_access_check.json"
    p_pt_net = ART / "pt" / "network_devices.json"
    p_pt_hosts = ART / "pt" / "hosts.json"

    # Load JSON
    webex_room_json = read_json(p_webex_room)
    pt_net_json = read_json(p_pt_net)
    pt_hosts_json = read_json(p_pt_hosts)

    # Checks
    yang_ok = contains(p_yang, "+--rw interfaces")
    webex_title_ok = json_contains(webex_room_json, th8)
    pt_empty_ticket_ok = contains(p_pt_ext, "empty ticket")
    pt_net_ok = json_contains(pt_net_json, '"version": "1.0"') or json_contains(pt_net_json, '"version":"1.0"')
    pt_hosts_ok = json_contains(pt_hosts_json, '"version": "1.0"') or json_contains(pt_hosts_json, '"version":"1.0"')
    pt_ok = pt_empty_ticket_ok and pt_net_ok and pt_hosts_ok

    summary = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": now_utc(),
        "student": {
            "token": student_token,
            "token_hash8": th8,
            "name": student_name,
            "group": student_group,
        },
        "yang": {
            "ok": yang_ok,
            "evidence_sha": {
                "ietf_interfaces": sha256_file(ART / "yang" / "ietf-interfaces.yang"),
                "pyang_version": sha256_file(ART / "yang" / "pyang_version.txt"),
                "pyang_tree": sha256_file(ART / "yang" / "pyang_tree.txt"),
            },
        },
        "webex": {
            "ok": webex_title_ok,
            "room_title_contains_hash8": webex_title_ok,
            "evidence_sha": {
                "me": sha256_file(ART / "webex" / "me.json"),
                "rooms_list": sha256_file(ART / "webex" / "rooms_list.json"),
                "room_create": sha256_file(ART / "webex" / "room_create.json"),
                "message_post": sha256_file(ART / "webex" / "message_post.json"),
                "messages_list": sha256_file(ART / "webex" / "messages_list.json"),
            },
        },
        "pt": {
            "ok": pt_ok,
            "empty_ticket_seen": pt_empty_ticket_ok,
            "evidence_sha": {
                "external_access_check": sha256_file(ART / "pt" / "external_access_check.json"),
                "service_ticket": sha256_file(ART / "pt" / "serviceTicket.txt"),
                "network_devices": sha256_file(ART / "pt" / "network_devices.json"),
                "hosts": sha256_file(ART / "pt" / "hosts.json"),
                "pt_internal_output": sha256_file(ART / "pt" / "pt_internal_output.txt"),
                "postman_collection": sha256_file(ART / "pt" / "postman_collection.json"),
                "postman_environment": sha256_file(ART / "pt" / "postman_environment.json"),
            },
        },
        "bonus": {
            "optional_ok": True,
            "evidence_sha": {},
        },
        "validation_passed": bool(yang_ok and webex_title_ok and pt_ok),
        "run": {
            "python": sys.version.split()[0],
            "platform": sys.platform,
        },
    }

    out = ART / "summary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["validation_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
