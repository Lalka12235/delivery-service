from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import AddressEntity


class AddressRepository(ABC):

    @abstractmethod
    def get_address_by_id(self,address_id: uuid.UUID) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def get_address_by_user_id(self,user_id: uuid.UUID) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def get_address_by_restaurant_id(self,restaurant_id: uuid.UUID) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def create_address(self,address: AddressEntity) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def update_address(self,address: AddressEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_address(self,address_id: uuid.UUID) -> bool:
        raise NotImplementedError