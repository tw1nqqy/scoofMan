from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String
from backend.app.database.db import Base


class GameHistory(Base):
    __tablename__ = "game_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    score: Mapped[int] = mapped_column(Integer)
    timestamp: Mapped[str] = mapped_column(String)

    user = relationship("User", back_populates="games")  # Аннотация строкой
