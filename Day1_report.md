# Day 1 Report — DevNet Sprint

## 1. Student
- Name: Khismatullin Rashid
- Group: IB-23-5B
- GitHub repo: https://github.com/enot124-web/devnet-day1-ib235b-khismatullin
- Day1 Token: D1-IB-23-5b-26-CE25

## 2. NetAcad progress (Module 1)
- Completed items: [1.1 / 1.2 / 1.3]
- 1.2 - Базовые команды администрирование системы Linux, по типу cd, ls, echo, cat. Были несколько команд, связанных с правами. Работа с файлами(перемещение, копирование, удаление). Системные команды: shutdown, date, проверка сети через ip address и ping, просмотр процессов через ps, работа с пакетами через apt-get, смена пароля через passwd
- 1.3 - Повторил базовый Python в DEVASC VM: запуск интерпретатора, создание и запуск простого скрипта hello-world.py. Потом разобрал  основные конструкции языка: переменные, строки, списки, словари, условия if/else, циклы for и while, а также чтение и запись файлов
- Screenshot(s): отдельно

## 3. VM evidence
- File: `artifacts/day1/env.txt` exists: Yes
- Screenshot(s): отдельно

## 4. Repo structure (must match assignment)
- `src/day1_api_hello.py` : Yes
- `tests/test_day1_api_hello.py` : Yes
- `schemas/day1_summary.schema.json` : Yes
- `artifacts/day1/summary.json` : Yes
- `artifacts/day1/response.json` : Yes

## 5. Commands run (paste EXACT output)
### 5.1 Script run
{
  "schema_version": "1.0",
  "generated_utc": "2026-03-10T05:48:22.636180+00:00",
  "student": {
    "token": "D1-IB-23-5b-26-CE25",
    "name": "Khismatullin",
    "group": "IB235B"
  },
  "api": {
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "status_code": 200,
    "validation_passed": true,
    "validation_errors": [],
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}

###5.2
1 passed in 0.23s


#6 What I learned today
научился работать в DEVASC VM, также повторил работу с github

#7 Problems & fixes
- Problem: Проблема была в том, что скрипт не запускался в DEVASC VM из-за несовместимости аннотаций типов с Python 3.8.
- Fix: Использовал запись tuple[...] и list[...], а затем исправил код, заменив на Tuple и List из модуля typing, после чего скрипт и тесты успешно выполнились.
