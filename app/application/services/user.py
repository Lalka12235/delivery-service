from app.domain.entity.user import UserID
from app.domain.exception.user import UserNotFound, UserAlreadyExist
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
        user_exist = self.user_repo.get_user_by_id(user.id)
        if user_exist:
            raise UserAlreadyExist()

        user_created = self.user_repo.create_user(user)
        return user_created

    def update_user(self,user: UserEntity) -> bool:
        user_exist = self.user_repo.get_user_by_id(user.id)
        if not user_exist:
            raise UserNotFound()

        user_updated = self.user_repo.update_user(user)
        return user_updated

    def delete_user(self,user_id: UserID) -> UserEntity:
        user_exist = self.user_repo.get_user_by_id(user_id)
        if not user_exist:
            raise UserNotFound()
        
        user_deleted = self.user_repo.delete_user(user_id)
        return user_deleted