import uuid
from abc import ABC,abstractmethod

from app.domain.entity.address import AddressID
from app.domain.entity.courier import CourierID
from app.domain.entity.dish import DishID
from app.domain.entity.ingredients import IngredientID
from app.domain.entity.order import OrderID
from app.domain.entity.order_item import OrderItemID
from app.domain.entity.product import ProductID
from app.domain.entity.restaurant import RestaurantID
from app.domain.entity.review import ReviewID
from app.domain.entity.shop import ShopID
from app.domain.entity.user import UserID


class UUIDGenerator(ABC):

    @abstractmethod
    def generate_user_id(self) -> UserID:
        raise NotImplementedError

    @abstractmethod
    def generate_shop_id(self) -> ShopID:
        raise NotImplementedError

    @abstractmethod
    def generate_review_id(self) -> ReviewID:
        raise NotImplementedError

    @abstractmethod
    def generate_restaurant_id(self) -> RestaurantID:
        raise NotImplementedError

    @abstractmethod
    def generate_product_id(self) -> ProductID:
        raise NotImplementedError

    @abstractmethod
    def generate_order_item_id(self) -> OrderItemID:
        raise NotImplementedError

    @abstractmethod
    def generate_order_id(self) -> OrderID:
        raise NotImplementedError

    @abstractmethod
    def generate_ingredient_id(self) -> IngredientID:
        raise NotImplementedError

    @abstractmethod
    def generate_dish_id(self) -> DishID:
        raise NotImplementedError

    @abstractmethod
    def generate_courier_id(self) -> CourierID:
        raise NotImplementedError

    @abstractmethod
    def generate_address_id(self) -> AddressID:
        raise NotImplementedError