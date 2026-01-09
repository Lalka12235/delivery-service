all = (
    'Base',
    'UserModel',
    'ShopModel',
    'ReviewModel',
    'RestaurantModel',
    'ProductModel',
    'OrderItemAssociationModel'
)

from app.infrastructure.db.models.base import Base
from app.infrastructure.db.models.user import UserModel
from app.infrastructure.db.models.shop import ShopModel
from app.infrastructure.db.models.review import ReviewModel
from app.infrastructure.db.models.restaurant import RestaurantModel
from app.infrastructure.db.models.product import ProductModel
from app.infrastructure.db.models.order_item import OrderItemAssociationModel