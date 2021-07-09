from dependency_injector import containers, providers

from src.infra.containers import UserContainer

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    user_container = providers.Container(UserContainer)


def init_app() -> Container:
    return Container()
