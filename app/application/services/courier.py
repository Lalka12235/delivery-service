from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity import OrderEntity
from app.domain.entity.courier import CourierID, CourierEntity
from app.domain.entity.order import OrderID
from app.domain.entity.user import UserID
from app.domain.enum import RoleType, CourierStatus, VehicleType
from app.domain.exception.base_exception import CourierNotFoundError, AccessDenied, BusinessError, OrderNotFoundError
from app.domain.exception.order import OrderNotFinished
from app.domain.interfaces.courier import CourierRepository
from app.domain.interfaces.order import OrderRepository


class CourierService:

    def __init__(
            self,
            courier_repo: CourierRepository,
            order_repo: OrderRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider,
    ):
        self.courier_repo = courier_repo
        self.order_repo = order_repo
        self.id_generator = id_generator
        self.id_provider = id_provider

    def get_courier_by_id(self, courier_id: CourierID) -> CourierEntity:
        courier = self.courier_repo.get_courier_by_id(courier_id)
        if not courier:
            raise CourierNotFoundError()

        return courier

    def get_courier_by_user_id(self, user_id: UserID) -> CourierEntity:
        courier = self.courier_repo.get_courier_by_user_id(user_id)
        if not courier:
            raise CourierNotFoundError()

        return courier

    def create_courier(self, courier: CourierEntity) -> CourierEntity:
        current_user = self.id_provider.get_current_user()
        if current_user.id != courier.user_id:
            raise AccessDenied()
        if not courier.user_id:
            raise BusinessError(detail='Сначала должен быть создан пользователь')
        courier.id = self.id_generator.generate_courier_id()
        return self.courier_repo.create_courier(courier)

    def update_courier(self, courier: CourierEntity) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.id != courier.user_id:
            raise AccessDenied()
        updated = self.courier_repo.update_courier(courier)
        if not updated:
            raise CourierNotFoundError()

        return updated

    def delete_courier(self, courier_id: CourierID) -> bool:
        current_user = self.id_provider.get_current_user()
        courier = self.get_courier_by_id(courier_id)
        if current_user.id != courier.user_id:
            raise AccessDenied()

        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()

        deleted = self.courier_repo.delete_courier(courier_id)
        if not deleted:
            raise CourierNotFoundError()

        return deleted

    def accept_order(self,order_id: OrderID,courier_id: CourierID) -> OrderEntity:
        order = self.order_repo.get_order_by_id(order_id)
        if not order:
            raise OrderNotFoundError()

        if order.courier_id:
            raise BusinessError(detail='Курьер уже назначен на заказ')

        courier = self.courier_repo.get_courier_by_id(courier_id)
        if not courier:
            raise CourierNotFoundError()

        if not courier.active:
            raise BusinessError(detail='Курьер не вышел на смену')

        if courier.status != CourierStatus.WAITING:
            raise BusinessError(detail='Курьер скорее всего выполняет заказ и не может взять другой')

        order.courier_id = courier.id
        return order

    def decline_order(self,order_id: OrderID,courier_id: CourierID) -> OrderEntity:
        order = self.order_repo.get_order_by_id(order_id)
        if not order:
            raise OrderNotFoundError()

        if order.courier_id:
            raise BusinessError(detail='Другой курьер назначен на заказ')

        courier = self.courier_repo.get_courier_by_id(courier_id)
        if not courier:
            raise CourierNotFoundError()

        if not courier.status:
            raise BusinessError(detail='Курьер не вышел на смену')

        if courier.status != CourierStatus.DELIVERY:
            raise BusinessError(detail='Курьеру нечего отменять,если он не доставляет заказ')

        order.courier_id = None
        return order