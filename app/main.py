from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base # DB 연결 및 모델 초기화
from routers import post # post.py에서 정의한 라우터

# DB 테이블을 생성하는 코드
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# post 라우터 등록
app.include_router(post.router)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}