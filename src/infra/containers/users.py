from dependency_injector import containers, providers

from src.domain.users.services import CreateUserService
from src.domain.users.repositories.user_repository import UserRepository


class UserContainer(containers.DeclarativeContainer):

    user_repository = providers.Factory(
        UserRepository
    )

    create_user_service = providers.Factory(
        CreateUserService,
        repository=user_repository
    )
