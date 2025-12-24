import uuid
from dataclasses import dataclass
from typing import NewType

from app.domain.entity.address import AddressID
from app.domain.enum import RoleType
from datetime import datetime


UserID = NewType('UserID',uuid.UUID)


@dataclass(slots=True,frozen=True)
class UserEntity:
    id: UserID
    first_name: str
    last_name: str
    date_birth: datetime
    email: str
    phone_number: str
    role: RoleType
    created_at: datetime
    address_id: AddressID

    def get_old(self) -> int:
        now = str(datetime.now()).split(' ')
        date = now[0].split('-')
        now_year = date[0]

        date_birth_year = str(self.date_birth).split(' ')[0].split('-')[0]

        return int(now_year) - int(date_birth_year)