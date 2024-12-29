from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL  # .env 파일에서 DB URL을 가져옵니다.

# SQLAlchemy 엔진을 생성하여 데이터베이스와 연결
engine = create_engine(DATABASE_URL)

# 세션을 관리할 세션 클래스를 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델 클래스의 기본 클래스로 사용할 Base 생성
Base = declarative_base()

# 데이터베이스 세션을 관리하는 함수 (FastAPI에서 Dependency Injection 사용)
def get_db():
    db = SessionLocal()  # 새로운 DB 세션을 생성
    try:
        yield db  # FastAPI에 DB 세션을 주입
    finally:
        db.close()  # 요청이 끝나면 DB 세션을 닫음
