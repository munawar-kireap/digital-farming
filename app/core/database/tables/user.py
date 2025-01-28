from app.core.database.tables.base import Base

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

schema = 'sample'

class User(Base):
    __tablename__ = "user"
    __table_args__ = {'schema': schema}


    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
        unique=True,
    )
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)