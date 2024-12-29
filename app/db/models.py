from sqlalchemy import Column, DateTime, Integer, String, func
from db.database import Base

class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(8), nullable=False) # 8글자
    content = Column(String(500), nullable=False) # 500글자
    created_at = Column(DateTime, default=func.now())  # 생성 시간
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # 수정 시간
    