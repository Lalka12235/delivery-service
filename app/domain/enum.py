from enum import Enum

class RoleType(Enum):
    DEFAULT = 'user'
    COURIER = 'courier'
    ADMIN = 'admin'


class OrderStatus(Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    COOKING = 'cooking'
    READY = 'ready'
    DELIVERY = 'delivery'
    DELIVERED = 'delivered'


class CourierStatus(Enum):
    WAITING = 'waiting'
    DELIVERY = 'delivery'


class VehicleType(Enum):
    CAR = 'car'
    WALK = 'walk'
    BICYCLE = 'bicycle'