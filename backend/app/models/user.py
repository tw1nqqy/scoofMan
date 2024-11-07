from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from backend.app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)

    games: Mapped[list["GameHistory"]] = relationship("GameHistory", back_populates="user")  # Аннотация строкой
