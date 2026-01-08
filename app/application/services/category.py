from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity.category import CategoryID, CategoryEntity
from app.domain.enum import RoleType
from app.domain.exception.base_exception import CategoryNotFoundError, AccessDenied
from app.domain.interfaces.category import CategoryRepository


class CategoryService:

    def __init__(
            self,
            category_repo: CategoryRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,
    ):
        self.category_repo = category_repo
        self.id_generator = id_generator
        self.id_provider = id_provider

    def get_category_by_id(self, category_id: CategoryID) -> CategoryEntity:
        category = self.category_repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFoundError()

        return category

    def get_category_by_title(self, title: str) -> CategoryEntity:
        category = self.category_repo.get_category_by_title(title)
        if not category:
            raise CategoryNotFoundError()

        return category

    def create_category(self, category: CategoryEntity) -> CategoryEntity:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()

        category.id = self.id_generator.generate_category_id()
        return self.category_repo.create_category(category)

    def update_category(self, category: CategoryEntity) -> bool:
        updated = self.category_repo.update_category(category)
        if not updated:
            raise CategoryNotFoundError()

        return updated

    def delete_category(self, category_id: CategoryID) -> bool:
        deleted = self.category_repo.delete_category(category_id)
        if not deleted:
            raise CategoryNotFoundError()

        return deleted