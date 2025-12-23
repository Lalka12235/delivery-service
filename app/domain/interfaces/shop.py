from abc import ABC,abstractmethod

from app.domain.entity import ShopEntity
from app.domain.entity.shop import ShopID


class ShopRepository(ABC):

    @abstractmethod
    def get_shop_by_id(self,shop_id: ShopID) -> ShopEntity:
        raise NotImplementedError

    @abstractmethod
    def get_shop_by_title(self,title: str) -> ShopEntity:
        raise NotImplementedError

    @abstractmethod
    def create_shop(self,shop: ShopEntity) -> ShopEntity:
        raise NotImplementedError

    @abstractmethod
    def update_shop(self,shop: ShopEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_shop(self,shop_id: ShopID) -> bool:
        raise NotImplementedError