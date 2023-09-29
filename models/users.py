from sqlalchemy import ForeignKey, Column, String, UniqueConstraint
from sqlalchemy.orm import relationship
from . import Base

class Users(Base):
  __tablename__ = "users"

  id = Column("id", String, primary_key=True, unique=True)
  name = Column("name", String, nullable=False)
  email = Column("email", String, nullable=False, unique=False)
  password = Column("password", String, nullable=False)

  portfolio = relationship("Portfolio", back_populates="user")

  __table_args__ = (UniqueConstraint("email", name="unique_email"),)

  def __init__(self, id, name, email, password):
    self.id = id
    self.name = name
    self.email = email
    self.password = password

  def __repr__(self):
    return f"<{self.id}> {self.name}: {self.email}: {self.password}"

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "password": self.password
      }
