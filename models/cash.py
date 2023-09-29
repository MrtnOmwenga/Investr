from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class CashAccount(Base):
    __tablename__ = 'cash_accounts'

    id = Column(String, primary_key=True)
    account_name = Column(String(255), nullable=False)
    account_type = Column(String(100))
    balance = Column(Float)
    currency = Column(String(10))

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="cash_accounts")

    def __init__(self, id, account_name, account_type, balance, currency, portfolio_id):
        self.id= id
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance
        self.currency = currency
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f"<{self.id}> {self.account_name}: {self.account_type}: {self.balance}: {self.currency}"
    
    def to_dict(self):
        return {
        "id": self.id,
        "account_name": self.account_name,
        "account_type": self.account_type,
        "balance": self.balance,
        "currency": self.currency
        }
