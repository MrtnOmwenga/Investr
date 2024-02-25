import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from . import Base

class FundData(Base):
  __tablename__ = 'funds'

  id = Column(String, primary_key=True)
  symbol = Column(String(10), unique=True, nullable=False)
  nav = Column(Float)
  date_purchased = Column(Date)

  def __init__(self, symbol, nav, date_purchased):
    self.id = str(uuid.uuid4())
    self.symbol = symbol
    self.nav = nav
    self.date_purchased = date_purchased

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
