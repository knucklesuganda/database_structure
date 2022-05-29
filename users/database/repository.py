from sqlalchemy.exc import NoResultFound

from database.exceptions import NotFoundException
from database.repository import Repository
from users.database.models import User


class UserRepository(Repository):
    def get(self, id: int):
        try:
            return self.session.query(User).filter_by(id=id).one()
        except NoResultFound as exc:
            raise NotFoundException(exc)

    def list(self):
        return self.session.query(User).all()

    def save(self, obj):
        self.session.add(obj)

    def update(self, obj):
        self.session.add(obj)
