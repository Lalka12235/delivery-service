from app.domain.entity.user import UserID
from app.domain.exception.user import UserNotFound
from app.domain.interfaces.user import UserRepository
from app.domain.entity import UserEntity


class UserService:

    def __init__(self,user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user_by_id(self,user_id: UserID) -> UserEntity:
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFound()

        return user

    def get_user_by_email(self,email: str) -> UserEntity:
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise UserNotFound()

        return user

    def create_user(self,user: UserEntity) -> UserEntity:
        return self.user_repo.create_user(user)

    def update_user(self,user: UserEntity) -> bool:
        updated = self.user_repo.update_user(user)
        if not updated:
            raise UserNotFound()
        return updated

    def delete_user(self,user_id: UserID) -> UserEntity:
        deleted = self.user_repo.delete_user(user_id)
        if not deleted:
            raise UserNotFound()
        return deleted