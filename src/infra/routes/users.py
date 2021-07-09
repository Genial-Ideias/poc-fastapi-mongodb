from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.config.containers import Container

from src.domain.users.models.user_models import CreateUserModel
from src.domain.users.services import (
    CreateUserService,
)

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}},
)


@router.post('/')
@inject
def create_user(user: CreateUserModel, service: CreateUserService = Depends(Provide[Container.user_container.create_user_service])):
    return service.create(user)

@router.get('/')
@inject
def list_users(service: CreateUserService = Depends(Provide[Container.user_container.create_user_service])):
    return service.list_users()
