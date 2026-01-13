from datetime import datetime, UTC

from app.domain.enum import OrderStatus
from app.infrastructure.db.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID, ForeignKey, Enum, DateTime
import uuid



class OrderModel(Base):
    __tablename__ = 'orders'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    description: Mapped[str] = mapped_column(nullable=True)
    cost: Mapped[int] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    order_item: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[OrderStatus] = mapped_column(Enum,nullable=True)
    delivery_time: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=True,default=datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True),nullable=False)
    restaurant_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey('restaurants.id'),nullable=False)
    shop_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey('shops.id'), nullable=False)
    courier_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey('couriers.id'), nullable=False)
    user_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey('users.id'), nullable=False)