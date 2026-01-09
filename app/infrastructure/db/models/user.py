from datetime import datetime,UTC

from app.domain.enum import RoleType
from app.infrastructure.db.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID,DateTime,ForeignKey
import uuid


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str | None] = mapped_column(nullable=False,default=None)
    date_birth: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=True)
    email: Mapped[str | None] = mapped_column(nullable=False,default=None)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    role: Mapped[RoleType] = mapped_column(nullable=True,default=RoleType.DEFAULT)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=True,default=datetime.now(UTC))
    address_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('address.id'),nullable=False)