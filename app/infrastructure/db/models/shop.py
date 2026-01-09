from app.infrastructure.db.models import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import UUID, ForeignKey
import uuid


class ShopModel(Base):
    __tablename__ = 'shops'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),primary_key=True)
    title: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    start_working_time: Mapped[str] = mapped_column(nullable=True)
    end_working_time: Mapped[str] = mapped_column(nullable=True)
    rating: Mapped[float] = mapped_column(nullable=True)
    address_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('address.id'),nullable=False)