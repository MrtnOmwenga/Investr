from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///users/user-data.db")

Session = sessionmaker(bind=engine)
session = Session()
