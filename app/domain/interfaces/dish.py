from abc import ABC,abstractmethod

from app.domain.entity import DishEntity
from app.domain.entity.dish import DishID
from app.domain.entity.restaurant import RestaurantID


class DishRepository(ABC):

    @abstractmethod
    def get_dish_by_id(self,dish_id: DishID) -> DishEntity:
        raise NotImplementedError

    @abstractmethod
    def get_dish_by_title(self,title: str) -> DishEntity:
        raise NotImplementedError

    @abstractmethod
    def get_dishes_by_restaurant_id(self,restaurant_id: RestaurantID) -> list[DishEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_dish(self,dish: DishEntity) -> DishEntity:
        raise NotImplementedError

    @abstractmethod
    def update_dish(self,dish: DishEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_dish(self,dish_id: DishID) -> bool:
        raise NotImplementedError