from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from schemas.post import PostCreate, Post  # Pydantic 모델을 사용하여 요청/응답 데이터 처리
from crud.post import create_post, get_post, update_post, delete_post  # CRUD 함수들

router = APIRouter()  # 라우터 객체 생성

# 특정 게시글을 조회하는 GET 요청
@router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):  # 게시글 ID와 DB 세션을 받아옴
    db_post = get_post(db=db, post_id=post_id)  # 게시글 조회
    if db_post is None:  # 게시글이 없으면
        raise HTTPException(status_code=404, detail="Post not found")  # 404 오류 발생
    return db_post  # 게시글 반환

# 새 게시글을 생성하는 POST 요청
@router.post("/posts/", response_model=Post)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):  # PostCreate 모델로 데이터를 받음
    return create_post(db=db, title=post.title, content=post.content)  # 게시글 생성 후 반환

# 게시글을 수정하는 PUT 요청
@router.put("/posts/{post_id}", response_model=Post)
def update_existing_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):  # 게시글 ID와 수정할 데이터
    db_post = update_post(db=db, post_id=post_id, title=post.title, content=post.content)  # 게시글 수정
    if db_post is None:  # 게시글이 없으면
        raise HTTPException(status_code=404, detail="Post not found")  # 404 오류 발생
    return db_post  # 수정된 게시글 반환

# 게시글을 삭제하는 DELETE 요청
@router.delete("/posts/{post_id}", response_model=None)
def delete_existing_post(post_id: int, db: Session = Depends(get_db)):  # 게시글 ID와 DB 세션을 받아옴
    db_post = delete_post(db=db, post_id=post_id)  # 게시글 삭제
    if db_post is None:  # 게시글이 없으면
        raise HTTPException(status_code=404, detail="Post not found")  # 404 오류 발생
    return {"detail": "Post deleted successfully"}  # 성공적으로 삭제된 경우 메시지 반환
