# SWE-2025 팀플

- `SRS`: [SRS_IEEE.pdf](/SRS_IEEE_template.pdf)
- `Project`: [pyproject.toml](src/lib/server/pyproject.toml)
- `Docker`: [Dockerfile](src/lib/server/Dockerfile)

## Prototype

<video src="https://private-user-images.githubusercontent.com/75429815/452204880-53b99358-ee80-4b7d-ae6f-43259505e285.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDkxOTYyNTQsIm5iZiI6MTc0OTE5NTk1NCwicGF0aCI6Ii83NTQyOTgxNS80NTIyMDQ4ODAtNTNiOTkzNTgtZWU4MC00YjdkLWFlNmYtNDMyNTk1MDVlMjg1Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA2MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNjA2VDA3NDU1NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE1NzczNTQ1ZWU4MDI5MzhiMTc1MGQyZDkxZWY2YWExZTM3NmNiNzdkM2Y5ZTM3ZGM3NjJiNDQ1MWIxNjM3NTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.vzWe2B-QbTQOZE9RCtJdWNSrsV3rgPP-MtdBnFAyhtk" controls muted></video>

![Prototype image](/static/prototype.png)

> 이 프로젝트는 Apple Inc.에서 제공하는 Apple Design Resources를 기반으로 한 시각 자료를 포함하고 있습니다. 해당 자료는 Apple Design Resources License(2023년 6월 21일자)의 조건에 따라 교육 목적(학교 과제)으로만 사용되었으며, 사용자 인터페이스 목업 제작 용도로만 활용되었습니다.

## RUN

### Backend

먼저 [.env](src/lib/server/.env)를 수정합니다.

```sh
$ cd src\lib\server           # 서버 파일 경로
$ .venv\Scripts\Activate.ps1  # 가상환경 활성화
$ python load_model.py        # 필요한 모델 준비
$ uvicorn main:app --host=127.0.0.1 --port=8001 --reload  # 또는 Docker 사용
```

### Frontend

```sh
$ npm install
$ npm run dev
```
