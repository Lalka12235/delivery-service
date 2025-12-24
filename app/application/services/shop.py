from app.domain.entity.shop import ShopID, ShopEntity
from app.domain.exception.base_exception import ShopNotFoundError
from app.domain.interfaces.shop import ShopRepository


class ShopService:

    def __init__(self,shop_repo: ShopRepository):
        self.shop_repo = shop_repo

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
        return self.shop_repo.create_shop(shop)

    def update_shop(self,shop: ShopEntity) -> bool:
        shop_updated = self.shop_repo.update_shop(shop)
        if not shop_updated:
            raise ShopNotFoundError()
        return shop_updated

    def delete_shop(self,shop_id: ShopID) -> bool:
        shop_deleted = self.shop_repo.delete_shop(shop_id)
        if not shop_deleted:
            raise ShopNotFoundError()
        return shop_deleted