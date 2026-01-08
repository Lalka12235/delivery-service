from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity.address import AddressID, AddressEntity
from app.domain.entity.restaurant import RestaurantID
from app.domain.entity.user import UserID
from app.domain.exception.base_exception import AddressNotFoundError, AccessDenied
from app.domain.interfaces.address import AddressRepository


class AddressService:

    def __init__(
            self,
            address_repo: AddressRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,
    ):
        self.address_repo = address_repo
        self.id_generator = id_generator
        self.id_provider = id_provider

    def get_address_by_id(self, address_id: AddressID) -> AddressEntity:
        address = self.address_repo.get_address_by_id(address_id)
        if not address:
            raise AddressNotFoundError()

        return address

    def get_address_by_user_id(self, user_id: UserID) -> AddressEntity:
        address = self.address_repo.get_address_by_user_id(user_id)
        if not address:
            raise AddressNotFoundError()

        return address

    def get_address_by_restaurant_id(self, restaurant_id: RestaurantID) -> AddressEntity:
        address = self.address_repo.get_address_by_restaurant_id(restaurant_id)
        if not address:
            raise AddressNotFoundError()

        return address

    def create_address(self, address: AddressEntity) -> AddressEntity:
        currest_user = self.id_provider.get_current_user()

        if currest_user.id != address.user_id:
            raise AccessDenied()

        address.id = self.id_generator.generate_address_id()
        return self.address_repo.create_address(address)

    def update_address(self, address: AddressEntity) -> bool:
        updated = self.address_repo.update_address(address)
        if not updated:
            raise AddressNotFoundError()

        return updated

    def delete_address(self, address_id: AddressID) -> bool:
        deleted = self.address_repo.delete_address(address_id)
        if not deleted:
            raise AddressNotFoundError()

        return deleted

    def generate_full_address(self,address_id: AddressID) -> str:
        address = self.address_repo.get_address_by_id(address_id)
        if not address:
            raise AddressNotFoundError()

        parts = [
            address.city,
            address.street,
            address.house_number,
            address.floor,
            address.apartment_number
        ]
        full_address = ", ".join([str(p) for p in parts if p])

        return full_address