from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity import DishEntity
from app.domain.entity.dish import DishID
from app.domain.entity.restaurant import RestaurantID
from app.domain.enum import RoleType
from app.domain.exception.base_exception import DishNotFoundError, AccessDenied
from app.domain.interfaces.dish import DishRepository


class DishService:

    def __init__(
            self,
            dish_repo: DishRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider
    ):
        self.dish_repo = dish_repo
        self.id_generator = id_generator
        self.id_provider = id_provider

    def get_dish_by_id(self, dish_id: DishID) -> DishEntity:
        dish = self.dish_repo.get_dish_by_id(dish_id)
        if not dish:
            raise DishNotFoundError()

        return dish

    def get_dish_by_title(self, title: str) -> DishEntity:
        dish = self.dish_repo.get_dish_by_title(title)
        if not dish:
            raise DishNotFoundError()

        return dish

    def get_dishes_by_restaurant_id(self, restaurant_id: RestaurantID) -> list[DishEntity]:
        dishes = self.dish_repo.get_dishes_by_restaurant_id(restaurant_id)
        if not dishes:
            return []

        return [dish for dish in dishes]

    def create_dish(self, dish: DishEntity) -> DishEntity:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()

        dish.id = self.id_generator.generate_dish_id()
        return self.dish_repo.create_dish(dish)

    def update_dish(self, dish: DishEntity) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()
        dish_updated = self.dish_repo.update_dish(dish)
        if not dish_updated:
            raise DishNotFoundError()

        return dish_updated

    def delete_dish(self, dish_id: DishID) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()
        dish_deleted = self.dish_repo.delete_dish(dish_id)
        if not dish_deleted:
            raise DishNotFoundError()

        return dish_deleted