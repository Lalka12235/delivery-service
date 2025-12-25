from abc import ABC,abstractmethod

from app.domain.entity import UserEntity
from app.domain.entity.user import UserID


class IDProvider(ABC):

    @abstractmethod
    def get_current_user_id(self) -> UserID:
        raise NotImplementedError

    @abstractmethod
    def get_current_user(self) -> UserEntity:
        raise NotImplementedError