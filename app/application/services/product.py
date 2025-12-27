from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity import ProductEntity
from app.domain.entity.product import ProductID
from app.domain.enum import RoleType
from app.domain.exception.base_exception import ProductNotFoundError, AccessDenied
from app.domain.interfaces.product import ProductRepository


class ProductService:

    def __init__(
            self,
            product_repo: ProductRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,
    ):
        self.product_repo = product_repo
        self.id_generator = id_generator
        self.id_provider = id_provider


    def get_product_by_id(self,product_id: ProductID) -> ProductEntity:
        product = self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError()

        return product

    def get_product_by_title(self, title: str) -> ProductEntity:
        product = self.product_repo.get_product_by_title(title)
        if not product:
            raise ProductNotFoundError()

        return product

    def create_product(self,product: ProductEntity) -> ProductEntity:
        product.id = self.id_generator.generate_product_id()
        return self.product_repo.create_product(product)

    def update_product(self, product: ProductEntity) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        product_updated = self.product_repo.update_product(product)
        if not product_updated:
            raise ProductNotFoundError()

        return product_updated

    def delete_product(self, product_id: ProductID) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        product_deleted = self.product_repo.delete_product(product_id)
        if not product_deleted:
            raise ProductNotFoundError()

        return product_deleted