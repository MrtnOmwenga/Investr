import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class OptionsDerivatives(Base):
    __tablename__ = 'options_derivatives'

    id = Column(String, primary_key=True)
    contract_name = Column(String(255), nullable=False)
    underlying_asset = Column(String(255))
    contract_type = Column(String(100))
    expiration_date = Column(Date)
    price = Column(Float)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="options_derivatives")

    def __init__(self, contract_name, underlying_asset, contract_type, expiration_date, price, portfolio_id):
        self.id = str(uuid.uuid4())
        self.contract_name = contract_name
        self.underlying_asset = underlying_asset
        self.contract_type = contract_type
        self.expiration_date = expiration_date
        self.price = price
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f"""<{self.id}>
                {self.contract_name}:
                {self.underlying_asset}:
                {self.contract_type}:
                {self.expiration_date}:
                {self.price}"""
    
    def to_dict(self):
        return {
        "id": self.id,
        "contract_name": self.contract_name,
        "underlying_asset": self.underlying_asset,
        "contract_type": self.contract_type,
        "expiration_date": self.expiration_date,
        "price": self.price
        }
