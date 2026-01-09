from datetime import datetime, UTC

from app.infrastructure.db.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID, ForeignKey,DateTime
import uuid


class ReviewModel(Base):
    __tablename__ = 'reviews'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    title: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[float] = mapped_column(nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'),nullable=True)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('orders.id'),nullable=True)
    courier_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('couriers.id'),nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=True,default=datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False)