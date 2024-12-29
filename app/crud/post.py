from sqlalchemy.orm import Session
from schemas.post import Post

# 게시글을 생성하는 함수
def create_post(db: Session, title: str, content: str):
    db_post = Post(title=title, content=content)  # 게시글 객체 생성
    db.add(db_post)  # 데이터베이스 세션에 추가
    db.commit()  # 커밋하여 DB에 반영
    db.refresh(db_post)  # 새로 생성된 게시글 객체를 DB에서 갱신
    return db_post  # 생성된 게시글 객체 반환

# 특정 게시글을 조회하는 함수
def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()  # ID로 게시글을 조회

# 게시글을 수정하는 함수
def update_post(db: Session, post_id: int, title: str, content: str):
    db_post = db.query(Post).filter(Post.id == post_id).first()  # 게시글을 ID로 조회
    if db_post:  # 게시글이 존재하면
        db_post.title = title  # 제목 수정
        db_post.content = content  # 내용 수정
        db.commit()  # 수정사항 DB에 반영
        db.refresh(db_post)  # DB에서 갱신된 데이터 반영
    return db_post  # 수정된 게시글 반환

# 게시글을 삭제하는 함수
def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()  # 게시글을 ID로 조회
    if db_post:  # 게시글이 존재하면
        db.delete(db_post)  # 게시글 삭제
        db.commit()  # 커밋하여 DB에 반영
    return db_post  # 삭제된 게시글 반환
