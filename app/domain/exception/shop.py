class ShopNotFound(Exception):
    def __init__(self,detail: str = 'Магазин не найден',**kwargs):
        super().__init__(detail,kwargs)


class ShopAlreadyExist(Exception):
    def __init__(self,detail: str = 'Магазин уже существует',**kwargs):
        super().__init__(detail,kwargs)