from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import RestaurantEntity


class RestaurantRepository(ABC):

    @abstractmethod
    def get_restaurant_by_id(self,restaurant_id: uuid.UUID) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def get_restaurant_by_title(self,title: str) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def add(self,restaurant: RestaurantEntity) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self,restaurant_id: uuid.UUID,restaurant: dict[str,Any]) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def delete(self,restaurant_id: uuid.UUID) -> RestaurantEntity:
        raise NotImplementedError