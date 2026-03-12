# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Khismatullin Rashid
- Group: IB-23-5B
- Token: D1-IB-23-5b-26-CE25
- Repo: https://github.com/enot124-web/devnet-day1-ib235b-khismatullin

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots: отдельно
- Postman screenshots: отдельно
- Python run screenshot: отдельно

## 3) Artifacts checklist
- artifacts/day3/books_before.json: Yes
- artifacts/day3/books_sorted_isbn.json: Yes
- artifacts/day3/mybook_post.json: Yes
- artifacts/day3/books_by_me.json: Yes
- artifacts/day3/add100_report.json: Yes
- artifacts/day3/postman_collection.json: Yes
- artifacts/day3/postman_environment.json: Yes
- artifacts/day3/curl_get_books.txt: Yes
- artifacts/day3/curl_get_books_isbn.txt: Yes
- artifacts/day3/curl_get_books_sorted.txt: Yes
- artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-12T06:48:04.770778+00:00",
  "student": {
    "token": "D1-IB-23-5b-26-CE25",
    "token_hash8": "6d934724",
    "name": "Khismatullin",
    "group": "IB235B"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "caef4c8ac090fabbc9547a9dedd71cb2db9ea5033f376d67292e360eef5ad670",
    "books_sorted_isbn": "d279b392a5d02a18991203b628cbec063576c0727d5bdc7b10a4cfb05603b6ca",
    "mybook_post": "584db0463e0563b01e0a73306da50647cfd98b0eba1b572e319ab3a93f063436",
    "books_by_me": "98505cdb4ef979d53338a2e9178baac1c9ddb44c638951530a76e836267da8c8",
    "add100_report": "fda9d45af17bbec62e2978969dcda56eb45bf06bbd3b284c0d5f80b7d37cdb48",
    "postman_collection": "0d3041103e6e49b4685e16cf8f8db31443aa8deca997745f519910e859116fcc",
    "postman_environment": "4b9e0b97990725fb11b2dd7d4ff727d33305375d100aaf5ae9f9da5dd336e91d",
    "curl_get_books": "7b2d2daa9acf483c3fabf6669daceb2361d6ad2637b42b916153ff80d6133ae4",
    "curl_get_books_isbn": "66c71d6abb780807d4b5ec473d4b81148b08819c1038da817019e9f6377b6874",
    "curl_get_books_sorted": "a7eb24d6030dcecc33ac65226fded3c01677ed752ef5cc6bb48aaaa42a24c303"
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}
```
### 4.2) Test
```text
3 passed in 1.02s
```

## 5) Problems & fixes
- Problem: Не был установлен faker, также были проблемы после выполнения лабораторной работы. При попытке создать книгу все значения были null
- Fix: перезагрузка лабораторной, установка faker
