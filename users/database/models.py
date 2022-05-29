from sqlalchemy import Column, String, Float, Integer

from database.database_setup import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False)
    balance = Column(Float, default=0)
