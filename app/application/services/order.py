from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity import OrderEntity, ProductEntity, DishEntity
from app.domain.entity.category import CategoryID
from app.domain.entity.courier import CourierID
from app.domain.entity.dish import DishID
from app.domain.entity.order import OrderID
from app.domain.entity.product import ProductID
from app.domain.entity.restaurant import RestaurantID
from app.domain.enum import OrderStatus
from app.domain.exception.base_exception import CategoryNotFoundError, OrderNotFoundError, AccessDenied, \
    ProductNotFoundError, DishNotFoundError, BusinessError
from app.domain.interfaces.category import CategoryRepository
from app.domain.interfaces.dish import DishRepository
from app.domain.interfaces.order import OrderRepository

from datetime import datetime

from app.domain.interfaces.product import ProductRepository


class OrderService:

    def __init__(
            self,
            order_repo: OrderRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,
            category_repo: CategoryRepository,
            product_repo: ProductRepository,
            dish_repo: DishRepository
    ):
        self.order_repo = order_repo
        self.id_generator = id_generator
        self.id_provider = id_provider
        self.category_repo = category_repo
        self.product_repo = product_repo
        self.dish_repo = dish_repo


    def _age_verification_for_ordering(self) -> bool:
        current_user = self.id_provider.get_current_user()
        current_user_age = current_user.get_old()
        if current_user_age < 18:
            return False
        return True

    def _check_adult_restriction(self,category_id: CategoryID) -> bool:
        category = self.category_repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFoundError()

        if category.adult and not self._age_verification_for_ordering():
            raise AccessDenied("В заказе товары 18+, а вам меньше 18 лет")
        return True

    def _validate_date_now(self) -> str:
        return datetime.now().strftime("%Y-%m-%d")

    def _check_order_status(self,order_id: OrderID) -> OrderStatus:
        order = self.order_repo.get_order_by_id(order_id)
        return order.status

    def _check_product_order(self,product_id: ProductID) -> ProductEntity:
        product = self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError()
        self._check_adult_restriction(product.category_id)
        return product

    def _check_dish_order(self,dish_id: DishID) -> DishEntity:
        dish = self.dish_repo.get_dish_by_id(dish_id)
        if not dish:
            raise DishNotFoundError()
        self._check_adult_restriction(dish.category_id)
        return dish

    def get_order_by_id(self,order_id: OrderID) -> OrderEntity:
        order = self.order_repo.get_order_by_id(order_id)
        if not order:
            raise OrderNotFoundError()
        return order

    def get_history_by_user(
            self,
            limit: int = 10,
            offset: int = 0
    ) -> list[OrderEntity]:
        user_id = self.id_provider.get_current_user_id()
        order_history = self.order_repo.get_history_by_user(user_id,limit,offset)
        if not order_history:
            return []

        return [order for order in order_history]

    def get_active_orders_by_restaurant(self, restaurant_id: RestaurantID) -> list[OrderEntity]:
        active_orders = self.order_repo.get_active_orders_by_restaurant(restaurant_id)
        if not active_orders:
            return []

        return [order for order in active_orders]

    def get_current_courier_order(self, courier_id: CourierID) -> OrderEntity:
        current_date = self._validate_date_now()
        current_order = self.order_repo.get_current_courier_order(courier_id,current_date)
        if not current_order:
            raise OrderNotFoundError()

        return current_order

    def create_order(self,order_data: OrderEntity) -> OrderEntity:
        total_sum = 0

        for order in order_data.order_item:
            product_id = order.product_id
            dish_id = order.dish_id

            if product_id:
                product = self._check_product_order(product_id)
                if product.shop_id != order_data.shop_id:
                    raise BusinessError()
                order.price_at_purchase = product.price
                total_sum += product.price * order.quantity

            elif dish_id:
                dish = self._check_dish_order(dish_id)
                if dish.restaurant_id != order_data.restaurant_id:
                    raise BusinessError()
                order.price_at_purchase = dish.price
                total_sum += dish.price * order.quantity

        order_data.id = self.id_generator.generate_order_id()
        order_data.cost = total_sum
        order_data.user_id = self.id_provider.get_current_user_id()
        order_data.status = OrderStatus.PENDING
        return self.order_repo.create_order(order_data)

    def update_order(self, order: OrderEntity) -> bool:
        order_status = self._check_order_status(order.id)
        if order_status == OrderStatus.ACCEPTED:
            raise BusinessError('Заказ уже нельзя изменить. Он принят')
        order_updated = self.order_repo.update_order(order)
        if not order_updated:
            raise OrderNotFoundError()

        return order_updated

    def delete_order(self,order_id: OrderID) -> bool:
        order_status = self._check_order_status(order_id)
        if order_status == OrderStatus.ACCEPTED:
            raise BusinessError('Заказ уже нельзя отменить. Он принят')
        order_deleted = self.order_repo.delete_order(order_id)
        if not order_deleted:
            raise OrderNotFoundError()

        return order_deleted