from dependency_injector.wiring import inject, Provide

from containers import Container
from database.exceptions import NotFoundException
from database.repository import Repository
from database.unit_of_work import UnitOfWork
from users.database.models import User


@inject
def list_users(repository: Repository = Provide[Container.users_repository]):
    return repository.list()


@inject
def get_user_by_id(id: int, repository: Repository = Provide[Container.users_repository]):
    try:
        return repository.get(id=id)
    except NotFoundException as exc:
        print("User not found: ", exc)
        return None


@inject
def create_user(username: str, unit_of_work: UnitOfWork = Provide[Container.users_uow]):
    with unit_of_work:
        new_user = User(username=username)
        print("New user created:", new_user.username)

        unit_of_work.repository.save(new_user)
        unit_of_work.commit()


@inject
def update_user_balance(
    id: int, balance_change: float, unit_of_work: UnitOfWork = Provide[Container.users_uow],
):
    with unit_of_work:
        user = unit_of_work.repository.get(id=id)
        user.balance += balance_change

        unit_of_work.repository.update(user)
        unit_of_work.commit()
