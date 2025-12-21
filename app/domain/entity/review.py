import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import NewType

ReviewID = NewType('ReviewID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class ReviewEntity:
    id: ReviewID
    title: str
    description: str
    rating: float
    user_id: uuid.UUID
    order_id: uuid.UUID
    courier_id: uuid.UUID
    created_at: datetime
    updated_at: datetime