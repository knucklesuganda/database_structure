from fastapi import APIRouter

from users.api.schemas import UserCreateSchema, UserUpdateSchema
from users.services import list_users, get_user_by_id, create_user, update_user_balance


router = APIRouter()


@router.get('/')
def list_users_route():
    return list_users()


@router.get('/{id}')
def get_user_route(id: int):
    return get_user_by_id(id=id)


@router.post('/')
def create_user_route(user_create: UserCreateSchema):
    create_user(user_create.username)
    return {"ack": True}


@router.patch('/update_balance/{id}')
def update_user_balance_route(id: int, user_update: UserUpdateSchema):
    update_user_balance(id=id, balance_change=user_update.balance_change)
    return {"ack": True}
