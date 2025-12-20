import uuid
from abc import ABC,abstractmethod
from typing import Any

from app.domain.entity import UserEntity


class UserRepository(ABC):

    @abstractmethod
    def get_user_by_id(self,user_id: uuid.UUID) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self,email: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def create_user(self,user: UserEntity) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def update_user(self,user: UserEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self,user_id: uuid.UUID) -> UserEntity:
        raise NotImplementedError