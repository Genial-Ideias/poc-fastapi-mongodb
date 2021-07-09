from dependency_injector import containers, providers

from src.domain.users.services import (
    CreateUserService,
)


class UserContainer(containers.DeclarativeContainer):

    db = providers.Dependency()

    create_user_service = providers.Factory(
        CreateUserService
    )
