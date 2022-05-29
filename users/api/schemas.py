from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str


class UserUpdateSchema(BaseModel):
    balance_change: float
