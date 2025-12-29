from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity.dish import DishID
from app.domain.entity.order import OrderID
from app.domain.entity.order_item import OrderItemID, OrderItemEntity
from app.domain.exception.base_exception import OrderItemNotFoundError
from app.domain.interfaces.order_item import OrderItemRepository


class OrderItemService:

    def __init__(
            self,
            order_item_repo: OrderItemRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,
    ):
        self.order_item_repo = order_item_repo
        self.id_generator = id_generator
        self.id_provider = id_provider

    def get_order_item_by_id(self, order_item_id: OrderItemID) -> OrderItemEntity:
        order_items = self.order_item_repo.get_order_item_by_id(order_item_id)
        if not order_items:
            raise OrderItemNotFoundError()

        return order_items

    def get_orders_items_by_order_id(self, order_id: OrderID) -> list[OrderItemEntity]:
        order_items = self.order_item_repo.get_orders_items_by_order_id(order_id)
        if not order_items:
            return []

        return [order_item for order_item in order_items]

    def get_orders_item_by_dish_id(self, dish_id: DishID) -> list[OrderItemEntity]:
        order_items = self.order_item_repo.get_orders_item_by_dish_id(dish_id)
        if not order_items:
            return []

        return [order_item for order_item in order_items]

    def create_order_item(self, order_item: OrderItemEntity) -> OrderItemEntity:
        order_item.id = self.id_generator.generate_order_item_id()
        return self.order_item_repo.create_order_item(order_item)