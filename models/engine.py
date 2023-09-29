from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mydb.db")

Session = sessionmaker(bind=engine)
session = Session()
