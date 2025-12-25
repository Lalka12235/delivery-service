from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity import ReviewEntity
from app.domain.entity.courier import CourierID
from app.domain.entity.review import ReviewID
from app.domain.entity.user import UserID
from app.domain.exception.base_exception import ReviewNotFoundError, OrderNotFoundError, AccessDenied
from app.domain.exception.order import OrderNotFinished
from app.domain.interfaces.order import OrderRepository
from app.domain.interfaces.review import ReviewRepository


class ReviewService:

    def __init__(
            self,
            review_repo: ReviewRepository,
            order_repo: OrderRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider
    ):
        self.review_repo = review_repo
        self.order_repo = order_repo
        self.id_generator = id_generator
        self.id_provider = id_provider


    def get_review_by_id(self,review_id: ReviewID) -> ReviewEntity:
        review = self.review_repo.get_review_by_id(review_id)
        if not review:
            raise ReviewNotFoundError()

        return review

    def get_review_by_title(self,title: str) -> ReviewEntity:
        review = self.review_repo.get_review_by_title(title)
        if not review:
            raise ReviewNotFoundError()

        return review

    def get_user_reviews_by_user_id(self,user_id: UserID) -> list[ReviewEntity]:
        reviews = self.review_repo.get_user_reviews_by_user_id(user_id)
        if not reviews:
            return []

        return [review for review in reviews]

    def get_courier_reviews_by_courier_id(self,courier_id: CourierID) -> list[ReviewEntity]:
        reviews = self.review_repo.get_courier_reviews_by_courier_id(courier_id)
        if not reviews:
            return []

        return [review for review in reviews]

    def create_review(self,review_data: ReviewEntity) -> ReviewEntity:
        exist_order = self.order_repo.get_order_by_id(review_data.order_id)
        if not exist_order:
            raise OrderNotFoundError()

        if exist_order.user_id != review_data.user_id:
            raise AccessDenied()

        if not exist_order.status.DELIVERED:
            raise OrderNotFinished()

        review_data.id = self.id_generator.generate_review_id()
        return self.review_repo.create_review(review_data)

    def update_review(self,review: ReviewEntity) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.id != review.user_id:
            raise AccessDenied()

        review_updated = self.review_repo.update_review(review)
        if not review_updated:
            raise ReviewNotFoundError()

        return review_updated

    def delete_review(self,review_id: ReviewID) -> bool:
        review = self.review_repo.get_review_by_id(review_id)
        if not review:
            raise ReviewNotFoundError()

        current_user = self.id_provider.get_current_user()
        if review.user_id != current_user.id:
            raise AccessDenied()

        review_deleted = self.review_repo.delete_review(review_id)
        if not review_deleted:
            raise ReviewNotFoundError()

        return review_deleted