from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.app.auth import (
    login_for_access_token,
    read_users_me,
    get_current_active_user,
)
from backend.app.database import get_db
from backend.app.schemas import Token, User

router = APIRouter()


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login_for_access_token(form_data, db)


@router.get("/users/me", response_model=User)
async def get_me(current_user: User = Depends(get_current_active_user)):
    return await read_users_me(current_user)
