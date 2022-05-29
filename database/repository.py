from abc import ABC, abstractmethod


class Repository(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def get(self, id: int):
        raise NotImplementedError()

    @abstractmethod
    def list(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, obj):
        raise NotImplementedError()

    @abstractmethod
    def update(self, obj):
        raise NotImplementedError()
