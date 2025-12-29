from abc import ABC,abstractmethod

from app.domain.entity import CategoryEntity
from app.domain.entity.category import CategoryID


class CategoryRepository(ABC):

    @abstractmethod
    def get_category_by_id(self,category_id: CategoryID) -> CategoryEntity:
        raise NotImplementedError