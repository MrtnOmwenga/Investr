from sqlalchemy import ForeignKey, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    user = relationship("Users", back_populates="portfolio")

    # Relationships with asset types
    stocks = relationship("Stock", back_populates="portfolio")
    bonds = relationship("Bond", back_populates="portfolio")
    real_estate = relationship("RealEstate", back_populates="portfolio")
    reits = relationship("REIT", back_populates="portfolio")
    private_equity = relationship("PrivateEquity", back_populates="portfolio")
    options_derivatives = relationship("OptionsDerivatives", back_populates="portfolio")
    funds = relationship("Fund", back_populates="portfolio")
    etfs = relationship("ETF", back_populates="portfolio")
    cryptocurrencies = relationship("Cryptocurrency", back_populates="portfolio")
    cash_accounts = relationship("CashAccount", back_populates="portfolio")

    def __init__(self, id, name, user_id):
        self.id = id
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"<{self.id}> {self.name}: {self.user_id}"
    
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "user_id": self.user_id,
        "user": self.user
        }

