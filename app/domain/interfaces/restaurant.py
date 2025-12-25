from abc import ABC,abstractmethod

from app.domain.entity import RestaurantEntity
from app.domain.entity.restaurant import RestaurantID


class RestaurantRepository(ABC):

    @abstractmethod
    def get_restaurant_by_id(self,restaurant_id: RestaurantID) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def get_restaurant_by_title(self,title: str) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def add(self,restaurant: RestaurantEntity) -> RestaurantEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self,restaurant: RestaurantEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self,restaurant_id: RestaurantID) -> bool:
        raise NotImplementedError