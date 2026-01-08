import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.address import Coordinates
from app.domain.entity.user import UserID
from app.domain.enum import CourierStatus, VehicleType

CourierID = NewType('CourierID',uuid.UUID)

@dataclass(slots=True)
class CourierEntity:
    id: CourierID
    status: CourierStatus
    active: bool
    rating: float
    cords: Coordinates
    vehicle_type: VehicleType
    user_id: UserID