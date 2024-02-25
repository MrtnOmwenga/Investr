import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Bond(Base):
    __tablename__ = 'bonds'

    id = Column(String, primary_key=True)
    issuer = Column(String(255), nullable=False)
    face_value = Column(Float)
    yield_rate = Column(Float)
    date_purchased = Column(Date)
    maturity_date = Column(Date)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="bonds")

    def __init__(self, issuer, face_value, yield_rate, date_purchased, maturity_date, portfolio_id):
        self.id = str(uuid.uuid4())
        self.issuer = issuer
        self.face_value = face_value
        self.yield_rate = yield_rate
        self.date_purchased = date_purchased
        self.maturity_date = maturity_date
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f"<{self.id}> {self.issuer}: {self.face_value}: {self.maturity_date}"

    def to_dict(self):
        return {
        "id": self.id,
        "issuer": self.issuer,
        "face_value": self.face_value,
        "yield_rate": self.yield_rate,
        "maturity_date": self.maturity_date
        }