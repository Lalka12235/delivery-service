from abc import ABC,abstractmethod
import uuid

from app.domain.entity import ShopEntity


class ShopRepository(ABC):

    @abstractmethod
    def get_shop_by_id(self,shop_id: uuid.UUID) -> ShopEntity:
        raise NotImplementedError

    @abstractmethod
    def get_shop_by_tile(self,title: str) -> ShopEntity:
        raise NotImplementedError

    @abstractmethod
    def create_shop(self,shop: ShopEntity) -> ShopEntity:
        raise NotImplementedError

    @abstractmethod
    def update_shop(self,shop: ShopEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_shop(self,shop_id: uuid.UUID) -> bool:
        raise NotImplementedError