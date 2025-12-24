from abc import ABC,abstractmethod

from app.domain.entity import UserEntity
from app.domain.entity.user import UserID


class UserRepository(ABC):

    @abstractmethod
    def get_user_by_id(self,user_id: UserID) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self,email: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_phone_number(self,phone_number: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def create_user(self,user: UserEntity) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def update_user(self,user: UserEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self,user_id: UserID) -> bool:
        raise NotImplementedError