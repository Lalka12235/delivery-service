class OrderNotFinished(Exception):

    def __init__(self,detail: str = 'Заказ еще не доставлен',**kwargs):
        super().__init__(detail,kwargs)