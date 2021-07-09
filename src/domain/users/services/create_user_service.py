from src.domain.users.models.user_models import CreateUserModel, UserModel

class CreateUserService:

    def create(self, create_user_model: CreateUserModel) -> UserModel:
        pass

    def _create(self, create_user_model: CreateUserModel) -> UserModel:
        pass
