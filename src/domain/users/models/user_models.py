from typing import Optional
from pydantic import BaseModel

from src.shared.models.pydantic_objectid import PydanticObjectId


class UserModel(BaseModel):
    id: PydanticObjectId
    name: str
    email: str
    password: Optional[str]

    class Config:
        orm_mode = True


class CreateUserModel(BaseModel):
    name: str
    email: str
    password: str

