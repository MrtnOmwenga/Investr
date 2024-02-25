import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(String, primary_key=True)
    symbol = Column(String(10), nullable=False)
    company_name = Column(String(255), nullable=False)
    quantity = Column(Float)
    price = Column(Float)
    date_purchased = Column(Date)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="stocks")

    def __init__(self, symbol, company_name, price, date_purchased, portfolio_id, quantity):
        self.id = str(uuid.uuid4())
        self.symbol = symbol
        self.company_name = company_name
        self.price = price
        self.date_purchased = date_purchased
        self.portfolio_id = portfolio_id
        self.quantity = quantity

    def __repr__(self):
        return f"<{self.id}> {self.symbol}: {self.company_name}: {self.date_purchased}"

    def to_dict(self):
        return {
        "id": self.id,
        "symbol": self.symbol,
        "company_name": self.company_name,
        "price": self.price,
        "date_purchased": self.date_purchased,
        "quantity": self.quantity
        }
