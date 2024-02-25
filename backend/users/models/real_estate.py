import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

class RealEstate(Base):
    __tablename__ = 'real_estate'

    id = Column(String, primary_key=True)
    property_name = Column(String(255), nullable=False)
    property_type = Column(String(100))
    value = Column(Float)
    location = Column(String(255))
    date_purchased = Column(Date)

    # Relationships
    portfolio_id = Column(String, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="real_estate")

    def __init__(self, property_type, property_name, value, location, portfolio_id, date_purchased):
        self.id = str(uuid.uuid4())
        self.property_name = property_name
        self.property_type = property_type
        self.value = value
        self.location = location
        self.portfolio_id = portfolio_id
        self.date_purchased = date_purchased

    def __repr__(self):
        return f"""<{self.id}>
                {self.property_type}:
                {self.property_name}:
                {self.value}:
                {self.location}:
                """
    
    def to_dict(self):
        return {
        "id": self.id,
        "property_type": self.property_type,
        "property_name": self.property_name,
        "value": self.value,
        "location": self.location
        }
