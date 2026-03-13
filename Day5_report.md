# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Khismatullin Rashid
- Group: IB-23-5B
- Token: D1-IB-23-5b-26-CE25
- Repo: https://github.com/enot124-web/devnet-day1-ib235b-khismatullin

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang - Yes
  - artifacts/day5/yang/pyang_version.txt - Yes
  - artifacts/day5/yang/pyang_tree.txt - Yes

## 3) Webex (8.6.7)
- Room title contains token_hash8: Yes/No
- Message text contains token_hash8: Yes/No
- Evidence files:
  - me.json / rooms_list.json / room_create.json / message_post.json / messages_list.json - Yes

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
  - external_access_check.json / network_devices.json / hosts.json - Yes
  - postman_collection.json / postman_environment.json - Yes
  - pt_internal_output.txt - Сломано

## 5) Commands output (paste exact)
```text
{
  "schema_version": "5.0",
  "generated_utc": "2026-03-13T07:08:28.165344+00:00",
  "student": {
    "token": "D1-IB-23-5b-26-CE25",
    "token_hash8": "6d934724",
    "name": "Khismatullin",
    "group": "IB235B"
  },
  "yang": {
    "ok": true,
    "evidence_sha": {
      "ietf_interfaces": "9a7aee5b007de501cbdbc6fc0139dd04b795695208f9d8c6e0fc0ffbad5184db",
      "pyang_version": "ad9fd0b80ba4e2b83161c31e379041a917955d5c462f18ebd97e142e38f2ead0",
      "pyang_tree": "949de5d3ee156508fe0af9f6a93bb6b16cf3e397ba9f6ba226e1c50bb5256edb"
    }
  },
  "webex": {
    "ok": true,
    "room_title_contains_hash8": true,
    "evidence_sha": {
      "me": "4d6c64a4ac53c38d70ac2bfe540193f67b668677a6e8a575b928d9d8f25b66c5",
      "rooms_list": "0343639fac1511a32a4c9a92c7655a6e9f9ad3a600fc6f30b5bdad6806160a97",
      "room_create": "a9053e7af2ef212a0bbd5fae947c75899f7df9c2520935002c84bd6d11fde9a4",
      "message_post": "5184d8f5050c7fb4153a1ccfd1cc39f49d19264c1290ed57df802c5815491342",
      "messages_list": "1d5bfd557cab0ed145a9c96919f277d7697b8faaa411cd49efa3be4fa62024d1"
    }
  },
  "pt": {
    "ok": true,
    "empty_ticket_seen": true,
    "evidence_sha": {
      "external_access_check": "17f0f971239431f07e62c6ba446e04c50a6ef25650e99d124e3d475c583c8446",
      "service_ticket": "bf5375bf725ede467529bc32e267d9db8d079e2dfc6202a1c0d70b91852759eb",
      "network_devices": "0477945380b2eea995dd58bca24de84ea31eb826989f0a952824cceed52c04cb",
      "hosts": "64f6debae3dd88d15a950f89a78dcfc10db829efb41407cd2f64cb1f1b9ee7f1",
      "pt_internal_output": "6370ac650d07b24c9526a577a58ff4936bd9dfa6412dc80368f24e8ed9507120",
      "postman_collection": "5f1a4fbc4ad56dd1b4527d0f8589f0cbfd197f63b6c96b7ace02c78a8685b089",
      "postman_environment": "281204cb737dec085280e3350e91a4b8f0713f04be0e9a52a4a1459a5c29de78"
    }
  },
  "bonus": {
    "optional_ok": true,
    "evidence_sha": {}
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}

```


```text
5 passed in 1.55s
```

## 6) Problems & fixes
Проблема: В Packet Tracer не работала вкладка Programming, а модуль Resource Script был отключён.

Исправление: Выполнил внешнюю часть PT Controller REST API через DEVASC VM, а ограничение внутреннего шага зафиксировал в pt_internal_output.txt.

Доказательство: В external_access_check.json есть empty ticket, сохранён serviceTicket.txt, а также получены network_devices.json и hosts.json. + Скрин отдельно
