from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import IngredientEntity


class IngredientRepository(ABC):

    @abstractmethod
    def get_ingredient_by_id(self,ingredient_id: uuid.UUID) -> IngredientEntity:
        raise NotImplementedError

    @abstractmethod
    def get_ingredient_by_title(self,title: str) -> IngredientEntity:
        raise NotImplementedError

    @abstractmethod
    def get_ingredients_by_dish_id(self,dish_id: uuid.UUID) -> list[IngredientEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_ingredient(self,ingredient: IngredientEntity) -> IngredientEntity:
        raise NotImplementedError

    @abstractmethod
    def update_ingredient(self,ingredient: IngredientEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_ingredient(self,ingredient_id: uuid.UUID) -> IngredientEntity:
        raise NotImplementedError