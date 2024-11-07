from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from backend.app.database.db import Base
from backend.app.models import User


class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    score: Mapped[int] = mapped_column(Integer)

    user: Mapped["User"] = relationship("User")
