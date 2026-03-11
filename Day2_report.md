# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: [Khismatullin Rashid]
- Group: [IB-23-5B]
- Token: [D1-IB-23-5b-26-CE25]
- Repo: https://github.com/enot124-web/devnet-day1-ib235b-khismatullin
- PR link (day2): https://github.com/enot124-web/devnet-day1-ib235b-khismatullin/pull/1

## 2) NetAcad progress
В модуле 2 была выполнена лабораторная работа по изучению ресурсов Cisco DevNet, в ходе которой были рассмотрены обучающие материалы, видеокурсы, sandboxes, Code Exchange и платформы разработчика. В модуле 3 были выполнены лабораторные работы, посвященные инструментам разработки на Python и основам автоматизации: изучены средства Python-разработки, работа с виртуальным окружением и пакетами, основы системы контроля версий Git и GitHub, принципы объектно-ориентированного программирования в Python, создание модульных тестов с использованием unittest, а также разбор различных форматов данных, включая XML, JSON и YAML.

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: Yes
- File `artifacts/day2/conflict_log.txt` exists: Yes
- Conflict note (1–2 lines): Конфликт возник в файле README.md, потому что в двух разных ветках была изменена одна и та же строка раздела Progress.

## 4) Generated artifacts (Day2)
- normalized.json: Yes
- normalized.yaml: Yes
- normalized.xml: Yes
- normalized.csv: Yes
- summary.json: Yes

## 5) Commands output (paste EXACT output)
### 5.1 Generator
```text
{
  "schema_version": "2.0",
  "generated_utc": "2026-03-11T10:57:34.410818+00:00",
  "student": {
    "token": "D1-IB-23-5b-26-CE25",
    "token_hash8": "6d934724",
    "name": "Khismatullin",
    "group": "IB235B"
  },
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_json_sha256": "e51373c67a73fc9e7fa4f7d63f113e24b2d4ace6db20e8809ef9a06b0c583ecc",
    "normalized_yaml_sha256": "aaf514441914711a3d7521cbf73d07150db534bb0a3b9f0506b7461d0d786bbf",
    "normalized_xml_sha256": "277d4391ec8f822f85e880218825c457386bac83fe89d58bc1fc30d8ea4b22f9",
    "normalized_csv_sha256": "2aa2b2c3efb4957d8f972b3451930004cc300c5bbff34171f1a0295eef59ce4f"
  },
  "computed": {
    "title_len": 18
  }
}

```

### 5.2 Test
2 passed in 0.57s

## 6) What i learned
Сегодня я повторил работу с Git и ветками, изучил преобразование данных в JSON, YAML, XML и CSV, а также автоматическую проверку скриптов с помощью pytest и schema.

## 7) Problem and fixes
Problem: При запуске скрипта day2_data_formats.py возникла ошибка ModuleNotFoundError: No module named 'yaml', потому что в виртуальном окружении не был установлен PyYAML.

Fix: Я установил зависимость командой pip install PyYAML, обновил окружение и повторно запустил скрипт и тесты. После этого генерация файлов normalized.json, normalized.yaml, normalized.xml, normalized.csv и проверка через pytest -q прошли успешно.


