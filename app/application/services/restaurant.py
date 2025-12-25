from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity.restaurant import RestaurantID, RestaurantEntity
from app.domain.enum import RoleType
from app.domain.exception.base_exception import RestaurantNotFoundError, AccessDenied
from app.domain.exception.restaurant import RestaurantHasNotFinishedOrdersError
from app.domain.interfaces.order import OrderRepository
from app.domain.interfaces.restaurant import RestaurantRepository


class RestaurantService:

    def __init__(
            self,
            restaurant_repo: RestaurantRepository,
            order_repo: OrderRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,

    ):
        self.restaurant_repo = restaurant_repo
        self.order_repo = order_repo
        self.id_generator = id_generator
        self.id_provider = id_provider


    def get_restaurant_by_id(self,restaurant_id: RestaurantID) -> RestaurantEntity:
        restaurant = self.restaurant_repo.get_restaurant_by_id(restaurant_id)
        if not restaurant:
            raise RestaurantNotFoundError()

        return restaurant

    def get_restaurant_by_title(self, title: str) -> RestaurantEntity:
        restaurant = self.restaurant_repo.get_restaurant_by_title(title)
        if not restaurant:
            raise RestaurantNotFoundError()

        return restaurant

    def add(self,restaurant: RestaurantEntity) -> RestaurantEntity:
        user = self.id_provider.get_current_user()
        if user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        restaurant.id = self.id_generator.generate_restaurant_id()
        return self.restaurant_repo.add(restaurant)

    def update(self,restaurant: RestaurantEntity) -> bool:
        user = self.id_provider.get_current_user()
        if user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        restaurant_updated = self.restaurant_repo.update(restaurant)
        if not restaurant_updated:
            raise RestaurantNotFoundError()

        return restaurant_updated

    def delete(self,restaurant_id: RestaurantID) -> bool:
        user = self.id_provider.get_current_user()
        if user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        restaurant_orders = self.order_repo.get_active_orders_by_restaurant(restaurant_id)
        if restaurant_orders:
            raise RestaurantHasNotFinishedOrdersError()

        restaurant_deleted = self.restaurant_repo.delete(restaurant_id)
        if not restaurant_deleted:
            raise RestaurantNotFoundError()

        return restaurant_deleted