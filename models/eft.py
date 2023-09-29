from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class ETF(Base):
    __tablename__ = 'etfs'

    id = Column(String, primary_key=True)
    symbol = Column(String(10), unique=True, nullable=False)
    fund_name = Column(String(255), nullable=False)
    price = Column(Float)
    date_purchased = Column(Date)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="etfs")

    def __init__(self, id, symbol, fund_name, price, date_purchased, portfolio_id):
        self.id = id
        self.symbol = symbol
        self.fund_name = fund_name
        self.price = price
        self.date_purchased = date_purchased
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f"<{self.id}> {self.symbol}: {self.fund_name}: {self.price}: {self.date_purchased}"
    
    def to_dict(self):
        return {
        "id": self.id,
        "fund_name": self.fund_name,
        "symbol": self.symbol,
        "price": self.price,
        "date_purchased": self.date_purchased
        }
