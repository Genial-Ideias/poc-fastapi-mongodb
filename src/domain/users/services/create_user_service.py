from src.domain.users.repositories.user_repository import UserRepository
from src.domain.users.models.user_models import CreateUserModel, UserModel

class CreateUserService:

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def create(self, create_user_model: CreateUserModel) -> UserModel:
        user = self._create(create_user_model)
        return user

    def _create(self, create_user_model: CreateUserModel) -> UserModel:
        user = self._repository.create(create_user_model)
        return user
