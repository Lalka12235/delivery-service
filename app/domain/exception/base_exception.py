class NotFoundError(Exception):
    entity_name: str = "Entity"

    def __init__(self,**kwargs):
        self.message = f"{self.entity_name} не найден"
        super().__init__(self.message,kwargs)

class AlreadyExists(Exception):
    entity_name: str = 'Object'

    def __init__(self,**kwargs):
        self.message = f"{self.entity_name} уже существует"
        super().__init__(self.message,kwargs)

class UserNotFoundError(NotFoundError):
    entity_name = "User"

class ShopNotFoundError(NotFoundError):
    entity_name = "Shop"

class ReviewNotFoundError(NotFoundError):
    entity_name = "Review"

class OrderNotFoundError(NotFoundError):
    entity_name = "Order"



class UserAlreadyExists(AlreadyExists):
    entity_name: str = 'User'

class ShopAlreadyExists(AlreadyExists):
    entity_name: str = 'Shop'

class ReviewAlreadyExists(AlreadyExists):
    entity_name: str = 'Review'


class AccessDenied(Exception):

    def __init__(self, detail: str = 'В доступе отказано', **kwargs):
        super().__init__(detail, kwargs)