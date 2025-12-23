class UserNotFound(Exception):
    def __init__(self,detail='Пользователь не найден',**kwargs):
        super().__init__(detail,kwargs)

class UserAlreadyExist(Exception):
    def __init__(self,detail='Пользователь уже существует',**kwargs):
        super().__init__(detail,kwargs)
