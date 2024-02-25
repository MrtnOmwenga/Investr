import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from . import Base

class StockData(Base):
    __tablename__ = 'stock_data'

    id = Column(String, primary_key=True)
    symbol = Column(String(10), nullable=False)
    price = Column(Float)
    date = Column(Date)

    def __init__(self, symbol, price, date):
        self.id = str(uuid.uuid4())
        self.symbol = symbol
        self.price = price
        self.date = date

    def __repr__(self):
        return f"<{self.id}> {self.symbol}: {self.price}: {self.date}"

    def to_dict(self):
        return {
        "id": self.id,
        "symbol": self.symbol,
        "price": self.price,
        "date": self.date,
        }