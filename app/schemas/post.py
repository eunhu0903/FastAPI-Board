from pydantic import BaseModel, Field
from datetime import datetime

# 게시글 기본 정보
class PostBase(BaseModel):
    title: str = Field(..., max_length=8, min_length=1, description="게시글 제목 (1~8자)")
    content: str = Field(..., max_length=500, min_length=1, description="게시글 내용 (1~500자)")

# 게시글 생성 요청 모델
class PostCreate(PostBase):
    """
    게시글 생성 요청에 사용되는 데이터 모델.
    """
    pass

# 게시글 응답 모델
class Post(PostBase):
    id: int = Field(..., description="게시글 고유 ID")  # 게시글 ID
    created_at: datetime = Field(..., description="게시글 생성 시간")  # 게시글 생성 시간
    updated_at: datetime = Field(..., description="게시글 수정 시간")  # 게시글 수정 시간

    class Config:
        from_attributes = True  # SQLAlchemy 모델에서 데이터 변환 활성화
