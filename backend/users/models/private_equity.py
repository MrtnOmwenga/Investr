import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class PrivateEquity(Base):
    __tablename__ = 'private_equity'

    id = Column(String, primary_key=True)
    fund_name = Column(String(255), nullable=False)
    date_invested = Column(Date)
    commitment_amount = Column(Float)
    current_value = Column(Float)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="private_equity")

    def __init__(self, fund_name, date_invested, commitment_amount, current_value, portfolio_id):
        self.id = str(uuid.uuid4())
        self.fund_name = fund_name
        self.date_invested = date_invested
        self.commitment_amount = commitment_amount
        self.current_value = current_value
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f"""<{self.id}>
                {self.fund_name}:
                {self.date_invested}:
                {self.commitment_amount}:
                {self.current_value}:
                """
    
    def to_dict(self):
        return {
        "id": self.id,
        "fund_name": self.fund_name,
        "date_invested": self.date_invested,
        "commitment_amount": self.commitment_amount,
        "current_value": self.current_value
        }
