from abc import ABC,abstractmethod

from app.domain.entity import CategoryEntity
from app.domain.entity.category import CategoryID


class CategoryRepository(ABC):

    @abstractmethod
    def get_category_by_id(self,category_id: CategoryID) -> CategoryEntity:
        raise NotImplementedError

    @abstractmethod
    def get_category_by_title(self,title: str) -> CategoryEntity:
        raise NotImplementedError

    @abstractmethod
    def create_category(self,category: CategoryEntity) -> CategoryEntity:
        raise NotImplementedError

    @abstractmethod
    def update_category(self,category: CategoryEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_category(self,category_id: CategoryID) -> bool:
        raise NotImplementedError