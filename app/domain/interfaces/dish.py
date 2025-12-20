from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import DishEntity


class DishRepository(ABC):

    @abstractmethod
    def get_dish_by_id(self,dish_id: uuid.UUID) -> DishEntity:
        raise NotImplementedError

    @abstractmethod
    def get_dish_by_title(self,title: str) -> DishEntity:
        raise NotImplementedError

    @abstractmethod
    def get_dishes_by_restaurant_id(self,restaurant_id: uuid.UUID) -> list[DishEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_dish(self,dish: DishEntity) -> DishEntity:
        raise NotImplementedError

    @abstractmethod
    def update_dish(self,dish: DishEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_dish(self,dish_id: uuid.UUID) -> bool:
        raise NotImplementedError