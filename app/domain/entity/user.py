import uuid
from dataclasses import dataclass
from app.domain.enum import RoleType
from datetime import datetime


@dataclass(slots=True,frozen=True)
class UserEntity:
    id: uuid.UUID
    first_name: str
    last_name: str
    date_birth: datetime
    email: str
    phone_number: str
    role: RoleType
    created_at: datetime
    address_id: uuid.UUID