from enum import StrEnum

from sqlalchemy import String, Boolean, func, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import datetime

Base = declarative_base()

class UserStatus(StrEnum):
    USER = "user"
    ADMIN = "admin"
    DEVELOPER = "developer"
    TESTER = "tester"
    MODERATOR = "moderator"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    first_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    second_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    is_premium: Mapped[bool] = mapped_column(Boolean, default=False)
    language_code: Mapped[str | None] = mapped_column(String(10), nullable=True)
    registered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    last_activity: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    is_banned: Mapped[bool] = mapped_column(Boolean, default=False)
    status: Mapped[UserStatus] = mapped_column(
        String(20),
        server_default=UserStatus.USER.value(),
        nullable=False
    )
    automat_registration: Mapped[bool] = mapped_column(Boolean, default=False)


