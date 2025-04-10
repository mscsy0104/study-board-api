## 📘 board-api
공부 및 실습용 간단한 게시판 API입니다. FastAPI 기반으로 게시글 작성, 조회, 수정, 삭제 기능을 제공합니다.


## 💾 설치
- Python 3.10+
- FastAPI
- SQLite3
- SQLAlchemy
- Pydantic

## ⚙️ requirements.txt
- fastapi==0.115.1
- uvicorn==0.34.0
- SQLAlchemy==2.0.29
- pydantic==2.11.2

## 📦 설치 및 실행
```
# 1. 가상환경 (선택)
python -m venv venv
source venv/bin/activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. 서버 실행
uvicorn main:app --reload
```

## 📚 주요 기능
|메서드|경로|설명|
|---|---|---|
|GET	|/read	|게시글 전체 조회|
|GET	|/read/{id}	|게시글 상세 조회|
|POST	|/create	|게시글 생성|
|PUT	|/update/{id}	|게시글 수정|
|PATCH|/delete/{id}|게시글 삭제|
|DELETE|	/delete/{id}|	게시글 삭제|


## 🧪 API 문서
서버 실행 후 브라우저에서 확인:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## 👨🏻‍💻 참고한 블로그
https://datamoney.tistory.com/category/Python/FastAPI#google_vignette