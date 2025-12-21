from abc import ABC,abstractmethod

from app.domain.entity.courier import CourierEntity, CourierID
from app.domain.entity.user import UserID


class CourierRepository(ABC):

    @abstractmethod
    def get_courier_by_id(self,courier_id: CourierID) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def get_courier_by_user_id(self,user_id: UserID) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def create_courier(self,courier: CourierEntity) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def update_courier(self,courier: CourierEntity) -> CourierEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_courier(self,courier_id: CourierID) -> CourierEntity:
        raise NotImplementedError