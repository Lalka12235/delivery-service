from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import OrderEntity


class OrderRepository(ABC):

    @abstractmethod
    def get_order_by_id(self,order_id: uuid.UUID) -> OrderEntity:
        raise NotImplementedError

    @abstractmethod
    def get_history_by_user(self, user_id: uuid.UUID, limit: int = 10, offset: int = 0) -> list[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_active_orders_by_restaurant(self, restaurant_id: uuid.UUID) -> list[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_current_courier_order(self, courier_id: uuid.UUID) -> OrderEntity | None:
        raise NotImplementedError

    @abstractmethod
    def create_order(self,order_data: OrderEntity) -> OrderEntity:
        raise NotImplementedError

    @abstractmethod
    def update_order(self,order_id: uuid.UUID,order_data: dict[str,Any]) -> OrderEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_order(self,order_id: uuid.UUID) -> OrderEntity:
        raise NotImplemented