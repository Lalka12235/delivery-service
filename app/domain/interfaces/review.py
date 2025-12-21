from abc import ABC,abstractmethod

from app.domain.entity import ReviewEntity
from app.domain.entity.courier import CourierID
from app.domain.entity.review import ReviewID
from app.domain.entity.user import UserID


class ReviewRepository(ABC):

    @abstractmethod
    def get_review_by_id(self,review_id: ReviewID) -> ReviewEntity:
        raise NotImplementedError

    @abstractmethod
    def get_review_by_title(self,title: str) -> ReviewEntity:
        raise NotImplementedError

    @abstractmethod
    def get_user_reviews_by_user_id(self,user_id: UserID) -> list[ReviewEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_courier_reviews_by_courier_id(self,courier_id: CourierID) -> list[ReviewEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_review(self,review_data: ReviewEntity) -> ReviewEntity:
        raise NotImplementedError

    @abstractmethod
    def update_review(self,review: ReviewEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_review(self,review_id: ReviewID) -> bool:
        raise NotImplementedError