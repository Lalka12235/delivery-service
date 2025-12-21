import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.enum import CourierStatus, VehicleType

CourierID = NewType('CourierID',uuid.UUID)

@dataclass(slots=True,frozen=True)
class CourierEntity:
    id: CourierID
    status: CourierStatus
    active: bool
    rating: float
    vehicle_type: VehicleType
    user_id: uuid.UUID