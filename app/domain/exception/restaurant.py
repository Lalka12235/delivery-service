class RestaurantHasNotFinishedOrdersError(Exception):

    def __init__(
            self,
            detail: str = 'У ресторана есть незаконченные заказы',
            **kwargs
    ):
        super().__init__(detail,kwargs)