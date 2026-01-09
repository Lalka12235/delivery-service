from app.infrastructure.db.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID, ForeignKey
import uuid


class OrderItemAssociationModel(Base):
    __tablename__ = 'order-items'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=True)
    price_at_purchase: Mapped[int] = mapped_column(nullable=True)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('orders.id'),UUID(as_uuid=True),nullable=True)
    dish_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('dishes.id'),UUID(as_uuid=True),nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('products.id'),UUID(as_uuid=True),nullable=False)