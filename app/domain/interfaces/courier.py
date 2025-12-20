from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity.courier import CourierEntity


class CourierRepository(ABC):

    @abstractmethod
    def get_courier_by_id(self,courier_id: uuid.UUID) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def get_courier_by_user_id(self,user_id: uuid.UUID) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def create_courier(self,courier: CourierEntity) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def update_courier(self,courier: CourierEntity) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_courier(self,courier_id: uuid.UUID) -> CourierEntity:
        raise NotImplementedError