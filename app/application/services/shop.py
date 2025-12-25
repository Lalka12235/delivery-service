from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity.shop import ShopID, ShopEntity
from app.domain.enum import RoleType
from app.domain.exception.base_exception import ShopNotFoundError, AccessDenied
from app.domain.interfaces.shop import ShopRepository


class ShopService:

    def __init__(
            self,
            shop_repo: ShopRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider
    ):
        self.shop_repo = shop_repo
        self.id_generator = id_generator
        self.id_provider = id_provider


    def get_shop_by_id(self,shop_id: ShopID) -> ShopEntity:
        shop = self.shop_repo.get_shop_by_id(shop_id)
        if not shop:
            raise ShopNotFoundError()

        return shop

    def get_shop_by_title(self,title: str) -> ShopEntity:
        shop = self.shop_repo.get_shop_by_title(title)
        if not shop:
            raise ShopNotFoundError()

        return shop

    def create_shop(self,shop: ShopEntity) -> ShopEntity:
        user = self.id_provider.get_current_user()
        if user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        shop.id = self.id_generator.generate_shop_id()
        return self.shop_repo.create_shop(shop)

    def update_shop(self,shop: ShopEntity) -> bool:
        user = self.id_provider.get_current_user()
        if user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        shop_updated = self.shop_repo.update_shop(shop)
        if not shop_updated:
            raise ShopNotFoundError()
        return shop_updated

    def delete_shop(self,shop_id: ShopID) -> bool:
        user = self.id_provider.get_current_user()
        if user.role != RoleType.ADMIN.value:
            raise AccessDenied()

        shop_deleted = self.shop_repo.delete_shop(shop_id)
        if not shop_deleted:
            raise ShopNotFoundError()
        return shop_deleted