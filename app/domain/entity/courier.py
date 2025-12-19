import uuid
from dataclasses import dataclass

from app.domain.enum import CourierStatus, VehicleType


@dataclass(slots=True,frozen=True)
class CourierEntity:
    id: uuid.UUID
    status: CourierStatus
    active: bool
    rating: float
    vehicle_type: VehicleType
    user_id: uuid.UUID