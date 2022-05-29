from sqlalchemy.exc import NoResultFound


class NotFoundException(NoResultFound):
    pass
