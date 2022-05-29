from sqlalchemy.orm import sessionmaker
from database.database_setup import engine

Session = sessionmaker(bind=engine)
