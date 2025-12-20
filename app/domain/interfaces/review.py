from abc import ABC,abstractmethod
import uuid
from typing import Any

from app.domain.entity import ReviewEntity


class ReviewRepository(ABC):

    @abstractmethod
    def get_review_by_id(self,rating_id: uuid.UUID) -> ReviewEntity:
        raise NotImplementedError

    @abstractmethod
    def get_review_by_title(self,title: str) -> ReviewEntity:
        raise NotImplementedError

    @abstractmethod
    def get_user_reviews_by_user_id(self,user_id: uuid.UUID) -> list[ReviewEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_courier_reviews_by_courier_id(self,courier_id: uuid.UUID) -> list[ReviewEntity]:
        raise NotImplementedError

    @abstractmethod
    def create_review(self,review_data: ReviewEntity) -> ReviewEntity:
        raise NotImplementedError

    @abstractmethod
    def update_review(self,review: ReviewEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_review(self,review_id: uuid.UUID) -> bool:
        raise NotImplementedError