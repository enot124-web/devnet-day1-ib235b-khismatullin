#!/usr/bin/env python3
import hashlib
import json
import os
from pathlib import Path

import requests

ART = Path("artifacts/day5/webex")
BASE = "https://webexapis.com/v1"


def dump(obj, path: Path):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]


def main():
    student_token = os.environ["STUDENT_TOKEN"].strip()
    webex_token = os.environ["WEBEX_TOKEN"].strip()
    th8 = token_hash8(student_token)

    headers = {
        "Authorization": f"Bearer {webex_token}",
        "Content-Type": "application/json",
    }

    ART.mkdir(parents=True, exist_ok=True)

    me = requests.get(f"{BASE}/people/me", headers=headers, timeout=20)
    me.raise_for_status()
    me_json = me.json()
    dump(me_json, ART / "me.json")

    rooms = requests.get(f"{BASE}/rooms", headers=headers, timeout=20)
    rooms.raise_for_status()
    rooms_json = rooms.json()
    dump(rooms_json, ART / "rooms_list.json")

    room_title = f"Day5 Room {th8}"
    room_create = requests.post(
        f"{BASE}/rooms",
        headers=headers,
        json={"title": room_title},
        timeout=20,
    )
    room_create.raise_for_status()
    room_create_json = room_create.json()
    dump(room_create_json, ART / "room_create.json")

    room_id = room_create_json["id"]
    message_text = f"Day5 message {th8}"
    message_post = requests.post(
        f"{BASE}/messages",
        headers=headers,
        json={"roomId": room_id, "text": message_text},
        timeout=20,
    )
    message_post.raise_for_status()
    message_post_json = message_post.json()
    dump(message_post_json, ART / "message_post.json")

    messages = requests.get(
        f"{BASE}/messages",
        headers=headers,
        params={"roomId": room_id, "max": 10},
        timeout=20,
    )
    messages.raise_for_status()
    messages_json = messages.json()
    dump(messages_json, ART / "messages_list.json")

    print("OK")
    print(f"room_title={room_title}")
    print(f"message_text={message_text}")


if __name__ == "__main__":
    main()
