from sqlalchemy.orm import Session
from db.repository.user import create_new_user
from schemas.user import UserCreate


def create_random_user(db: Session):
    user = UserCreate(email="razp@mail.ru", password="hello")
    user = create_new_user(user=user, db=db)
    return user