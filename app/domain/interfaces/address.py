from abc import ABC,abstractmethod

from app.domain.entity import AddressEntity
from app.domain.entity.address import AddressID
from app.domain.entity.restaurant import RestaurantID
from app.domain.entity.user import UserID


class AddressRepository(ABC):

    @abstractmethod
    def get_address_by_id(self,address_id: AddressID) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def get_address_by_user_id(self,user_id: UserID) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def get_address_by_restaurant_id(self,restaurant_id: RestaurantID) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def create_address(self,address: AddressEntity) -> AddressEntity:
        raise NotImplementedError

    @abstractmethod
    def update_address(self,address: AddressEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_address(self,address_id: AddressID) -> bool:
        raise NotImplementedError