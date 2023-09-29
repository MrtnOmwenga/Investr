from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Fund(Base):
    __tablename__ = 'funds'

    id = Column(String, primary_key=True)
    fund_name = Column(String(255), nullable=False)
    symbol = Column(String(10), unique=True, nullable=False)
    nav = Column(Float)
    date_purchased = Column(Date)

    # Add a fund_type field to distinguish between Mutual, Index, and Hedge Funds
    fund_type = Column(String(50), nullable=False)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="funds")

    def __init__(self, id, symbol, fund_name, nav, date_purchased, portfolio_id, fund_type):
        self.id = id
        self.symbol = symbol
        self.fund_name = fund_name
        self.nav = nav
        self.date_purchased = date_purchased
        self.portfolio_id = portfolio_id
        self.fund_type = fund_type

    def __repr__(self):
        return f"<{self.id}> {self.symbol}: {self.fund_name}: {self.nav}: {self.date_purchased}"
    
    def to_dict(self):
        return {
        "id": self.id,
        "fund_name": self.fund_name,
        "symbol": self.symbol,
        "nav": self.nav,
        "date_purchased": self.date_purchased
        }
