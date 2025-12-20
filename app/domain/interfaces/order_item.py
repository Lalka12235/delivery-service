from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import OrderItemEntity


class OrderItemRepository(ABC):

    @abstractmethod
    def get_orders_item_by_id(self,order_item_id: uuid.UUID) -> list[OrderItemEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_orders_items_by_order_id(self,order_id: uuid.UUID) -> list[OrderItemEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_orders_item_by_dish_id(self,dish_id: uuid.UUID) -> list[OrderItemEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_order_item(self,order_item: OrderItemEntity) -> OrderItemEntity:
        raise NotImplementedError

    @abstractmethod
    def update_order_item(self,order_item: OrderItemEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_order_item(self,order_item_id: uuid.UUID) -> bool:
        raise NotImplementedError