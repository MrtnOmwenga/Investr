import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'

    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    symbol = Column(String(10), nullable=False)
    quantity = Column(Float)
    price = Column(Float)
    date_purchased = Column(Date)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="cryptocurrencies")

    def __init__(self, name, symbol, price, date_purchased, portfolio_id, quantity):
        self.id = str(uuid.uuid4())
        self.name = name
        self.symbol = symbol
        self.price = price
        self.date_purchased = date_purchased
        self.portfolio_id = portfolio_id
        self.quantity = quantity

    def __repr__(self):
        return f"<{self.id}> {self.name}: {self.symbol}: {self.price}: {self.quantity}: {self.date_purchased}"
    
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "symbol": self.symbol,
        "price": self.price,
        "date_purchased": self.date_purchased,
        "quantity": self.quantity
        }
