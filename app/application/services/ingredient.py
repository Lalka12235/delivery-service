from app.application.ports.id_generator import UUIDGenerator
from app.application.ports.id_provider import IDProvider
from app.domain.entity.dish import DishID
from app.domain.entity.ingredients import IngredientID, IngredientEntity
from app.domain.enum import RoleType
from app.domain.exception.base_exception import IngredientNotFoundError, AccessDenied
from app.domain.interfaces.ingredient import IngredientRepository


class IngredientService:

    def __init__(
            self,
            ingredient_repo: IngredientRepository,
            id_generator: UUIDGenerator,
            id_provider: IDProvider
    ):
        self.ingredient_repo = ingredient_repo
        self.id_generator = id_generator
        self.id_provider = id_provider

    def get_ingredient_by_id(self, ingredient_id: IngredientID) -> IngredientEntity:
        ingredient = self.ingredient_repo.get_ingredient_by_id(ingredient_id)
        if not ingredient:
            raise IngredientNotFoundError()

        return ingredient

    def get_ingredient_by_title(self, title: str) -> IngredientEntity:
        ingredient = self.ingredient_repo.get_ingredient_by_title(title)
        if not ingredient:
            raise IngredientNotFoundError()

        return ingredient

    def get_ingredients_by_dish_id(self, dish_id: DishID) -> list[IngredientEntity]:
        ingredients = self.ingredient_repo.get_ingredients_by_dish_id(dish_id)
        if not ingredients:
            return []

        return [ingredient for ingredient in ingredients]

    def create_ingredient(self, ingredient: IngredientEntity) -> IngredientEntity:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()

        ingredient.id = self.id_generator.generate_ingredient_id()
        return self.ingredient_repo.create_ingredient(ingredient)

    def update_ingredient(self, ingredient: IngredientEntity) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()
        ingredient_updated = self.ingredient_repo.update_ingredient(ingredient)
        if not ingredient_updated:
            raise IngredientNotFoundError()

        return ingredient_updated

    def delete_ingredient(self, ingredient_id: IngredientID) -> bool:
        current_user = self.id_provider.get_current_user()
        if current_user.role != RoleType.ADMIN:
            raise AccessDenied()
        ingredient_deleted = self.ingredient_repo.delete_ingredient(ingredient_id)
        if not ingredient_deleted:
            raise IngredientNotFoundError()

        return ingredient_deleted
