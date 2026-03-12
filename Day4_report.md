# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Khismatullin Rashid
- Group: IB-23-5B
- Token: D1-IB-23-5b-26-CE25
- Repo: https://github.com/enot124-web/devnet-day1-ib235b-khismatullin

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: Yes
- artifacts/day4/docker/sampleapp_token_proof.txt: Yes
- artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
- artifacts/day4/docker/sampleapp_build_log.txt: Yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: Yes
- artifacts/day4/jenkins/buildapp_console.txt: Yes
- artifacts/day4/jenkins/testapp_console.txt: Yes
- artifacts/day4/jenkins/pipeline_script.groovy: Yes
- artifacts/day4/jenkins/pipeline_console.txt: Yes
- artifacts/day4/jenkins/jenkins_url.txt: Yes

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: Yes
- artifacts/day4/ansible/ansible_hello.txt: Yes
- artifacts/day4/ansible/ansible_playbook_install.txt: Yes
- artifacts/day4/ansible/ports_conf_after.txt: Yes
- artifacts/day4/ansible/curl_apache_8081.txt Yes:

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: Yes
- artifacts/day4/security/login_v1.txt: Yes
- artifacts/day4/security/signup_v2.txt: Yes
- artifacts/day4/security/login_v2.txt: Yes
- artifacts/day4/security/db_tables.txt: Yes
- artifacts/day4/security/db_user_hash_sample.txt: Yes

## 3) Commands output
```text
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-12T14:41:52.845678+00:00",
  "student": {
    "token": "D1-IB-23-5b-26-CE25",
    "token_hash8": "6d934724",
    "name": "Khismatullin",
    "group": "IB235B"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "7b954bf834a3c66deb53a85fb6020d9c71071616e336210076c53a60edd8b54f",
    "docker_ps": "f7aff76c2d51d4f096b4ec5e61dc878731f0f791f321bf723a678846ec57fb93",
    "docker_build_log": "d5febf167d1a84fb9646c3e211b12e6235aa56bb108d905815736b452d43dbc6",
    "docker_token_proof": "cecfa5f2e436aee406c226ab725eb42d4e320449d38fb0e9d57af98f6108d788",
    "jenkins_docker_ps": "a9a76a01fb61855790cc5a09d5ae14c727a8bf544c5f95a4448c75ba9fde32b6",
    "buildapp_console": "85d0080f021b902c1f8a1401e9a16b3841f3df1a6745f78abf32f840be6cc7ee",
    "testapp_console": "1eb6dc08643c4b8802b901fef18700900dda84da066e9b5d135c7402a20f865e",
    "pipeline_script": "ebd828aaaae6bc90a3c96285189ba2e84c4bc3ef3a8da58dabb749a4ab189ca9",
    "pipeline_console": "f3a2963acf6389bc26c73259db41ff4a2b0f728755bf82b28c29398c514a7026",
    "jenkins_url": "185f195598830dbc315eb3a6741f97eace245e9d9d2a7225c5da77b87f27f3fc",
    "ansible_ping": "005e9245df2c530d64aee6bfec751dfc3ced4b06361f597e7fde4163bc44fd69",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "52e8a937db27c2f3d2326ca2c241fe2a2ba3de80bc689c286e6699d33342b771",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v1": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "signup_v2": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v2": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "db_tables": "ad86a4abb22eb668b27efd841c9da481b1681020c8b71ebcfcf570d81ef41ee2",
    "db_user_hash_sample": "21aa0b040100127b08679ce94f1733a3d712c2674e96f5a5031b1474bbe58965"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```

```text
4 passed in 0.76s
```

## 4) Short reflection
Самой сложной частью сегодня был Jenkins, потому что контейнер в виртуальной машине сначала не запускался и выдавал ошибки, связанные с потоками и ограничениями среды. Пришлось отдельно разбираться с параметрами запуска Docker и ресурсами виртуальной машины. Docker и Ansible прошли проще, потому что их ошибки было легче определить и исправить.

## 5)
- Проблема: Jenkins-контейнер не запускался и не открывался на localhost:8080.

- Исправление: Увеличил ресурсы виртуальной машины и изменил параметры запуска Docker для Jenkins.

- Доказательство: Jenkins успешно открылся в браузере, задания были созданы, а evidence-файлы сохранены в artifacts/day4/jenkins/.
