from app.infrastructure.db.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID, ForeignKey
import uuid


class ProductModel(Base):
    __tablename__ = 'products'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    title: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=True)
    weight: Mapped[float] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    shop_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('shops.id'),UUID(as_uuid=True),nullable=True)
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('categories.id'),UUID(as_uuid=True),nullable=True)