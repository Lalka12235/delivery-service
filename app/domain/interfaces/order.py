from abc import ABC,abstractmethod

from app.domain.entity import OrderEntity
from app.domain.entity.courier import CourierID
from app.domain.entity.order import OrderID
from app.domain.entity.restaurant import RestaurantID
from app.domain.entity.user import UserID


class OrderRepository(ABC):

    @abstractmethod
    def get_order_by_id(self,order_id: OrderID) -> OrderEntity:
        raise NotImplementedError

    @abstractmethod
    def get_history_by_user(self, user_id: UserID, limit: int = 10, offset: int = 0) -> list[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_active_orders_by_restaurant(self, restaurant_id: RestaurantID) -> list[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_current_courier_order(self, courier_id: CourierID) -> OrderEntity | None:
        raise NotImplementedError

    @abstractmethod
    def create_order(self,order_data: OrderEntity) -> OrderEntity:
        raise NotImplementedError

    @abstractmethod
    def update_order(self,order: OrderEntity) -> OrderEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_order(self,order_id: OrderID) -> OrderEntity:
        raise NotImplemented