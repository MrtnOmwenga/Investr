from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class REIT(Base):
    __tablename__ = 'reits'

    id = Column(String, primary_key=True)
    property_name = Column(String(255), nullable=False)
    symbol = Column(String(10), unique=True, nullable=False)
    price_per_share = Column(Float)
    date_purchased = Column(Date)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="reits")

    def __init__(self, id, property_name, symbol, price_per_share, date_purchased, portfolio_id):
        self.id = id
        self.property_name = property_name
        self.symbol = symbol
        self.price_per_share = price_per_share
        self.date_purchased = date_purchased
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f"""<{self.id}>
                {self.property_name}:
                {self.symbol}:
                {self.price_per_share}:
                {self.date_purchased}:
                """
    
    def to_dict(self):
        return {
        "id": self.id,
        "property_name": self.property_name,
        "date_purchased": self.date_purchased,
        "price_per_share": self.price_per_share,
        "symbol": self.symbol
        }
