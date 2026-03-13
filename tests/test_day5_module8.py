import hashlib
import json
import os
import subprocess
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "day5"
SCHEMA = ROOT / "schemas" / "day5_summary.schema.json"


def jload(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]


def test_day5_summary_and_artifacts():
    env = os.environ.copy()
    assert env.get("STUDENT_TOKEN")
    assert env.get("STUDENT_NAME")
    assert env.get("STUDENT_GROUP")

    result = subprocess.run(
        ["python", "src/day5_summary_builder.py"],
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode in (0, 2), result.stderr

    summary_path = ART / "summary.json"
    assert summary_path.exists()

    summary = jload(summary_path)
    schema = jload(SCHEMA)
    jsonschema.validate(instance=summary, schema=schema)

    th8 = token_hash8(env["STUDENT_TOKEN"])
    assert summary["student"]["token_hash8"] == th8

    required_files = [
        ART / "yang" / "ietf-interfaces.yang",
        ART / "yang" / "pyang_version.txt",
        ART / "yang" / "pyang_tree.txt",
        ART / "webex" / "me.json",
        ART / "webex" / "rooms_list.json",
        ART / "webex" / "room_create.json",
        ART / "webex" / "message_post.json",
        ART / "webex" / "messages_list.json",
        ART / "pt" / "external_access_check.json",
        ART / "pt" / "serviceTicket.txt",
        ART / "pt" / "network_devices.json",
        ART / "pt" / "hosts.json",
        ART / "pt" / "pt_internal_output.txt",
        ART / "pt" / "postman_collection.json",
        ART / "pt" / "postman_environment.json",
    ]

    for path in required_files:
        assert path.exists(), f"missing file: {path}"
        assert path.stat().st_size > 0, f"empty file: {path}"

    pyang_tree = (ART / "yang" / "pyang_tree.txt").read_text(encoding="utf-8", errors="replace")
    assert "+--rw interfaces" in pyang_tree

    room_create_text = (ART / "webex" / "room_create.json").read_text(encoding="utf-8", errors="replace")
    assert th8 in room_create_text

    ext_check_text = (ART / "pt" / "external_access_check.json").read_text(encoding="utf-8", errors="replace")
    assert "empty ticket" in ext_check_text.lower()

    network_devices_text = (ART / "pt" / "network_devices.json").read_text(encoding="utf-8", errors="replace")
    hosts_text = (ART / "pt" / "hosts.json").read_text(encoding="utf-8", errors="replace")
    assert '"version": "1.0"' in network_devices_text or '"version":"1.0"' in network_devices_text
    assert '"version": "1.0"' in hosts_text or '"version":"1.0"' in hosts_text

    assert summary["yang"]["ok"] is True
    assert summary["webex"]["room_title_contains_hash8"] is True
    assert summary["pt"]["empty_ticket_seen"] is True
