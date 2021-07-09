from typing import List
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

        user_model = UserModel.from_orm(user)

        return user_model

    def list_users(self) -> List[UserModel]:

        users = User.objects()
        ressults = [ UserModel.from_orm(user) for user in users ]
        return ressults
