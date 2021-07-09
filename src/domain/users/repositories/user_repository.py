from src.infra.orm.entities import User

from src.domain.users.models import CreateUserModel, UserModel

class UserRepository:

    def create(self, model: CreateUserModel) -> UserModel:
        user = User(
            name=model.name,
            email=model.email,
            password=model.password
        )

        user.save()

        user_model = UserModel(
            id=str(user.id),
            name=user.name,
            email=user.email,
            password=user.password
        )

        return user_model
