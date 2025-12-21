from abc import ABC,abstractmethod

from app.domain.entity import ProductEntity
from app.domain.entity.product import ProductID


class ProductRepository(ABC):

    @abstractmethod
    def get_product_by_id(self,product_id: ProductID) -> ProductEntity:
        raise NotImplementedError

    @abstractmethod
    def get_product_by_title(self,title: str) -> ProductEntity:
        raise NotImplementedError

    @abstractmethod
    def create_product(self,product: ProductEntity) -> ProductEntity:
        raise NotImplementedError

    @abstractmethod
    def update_product(self,product: ProductEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_product(self,product_id: ProductID) -> bool:
        raise NotImplementedError