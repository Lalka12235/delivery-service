from abc import ABC,abstractmethod

from app.domain.entity import OrderItemEntity
from app.domain.entity.dish import DishID
from app.domain.entity.order import OrderID
from app.domain.entity.order_item import OrderItemID


class OrderItemRepository(ABC):

    @abstractmethod
    def get_orders_item_by_id(self,order_item_id: OrderItemID) -> list[OrderItemEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_orders_items_by_order_id(self,order_id: OrderID) -> list[OrderItemEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_orders_item_by_dish_id(self,dish_id: DishID) -> list[OrderItemEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_order_item(self,order_item: OrderItemEntity) -> OrderItemEntity:
        raise NotImplementedError

    @abstractmethod
    def update_order_item(self,order_item: OrderItemEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_order_item(self,order_item_id: OrderItemID) -> bool:
        raise NotImplementedError