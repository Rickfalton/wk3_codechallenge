from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f"Band('{self.name}', '{self.hometown}')"
    
    def __str__(self):
        return f"{self.name} from {self.hometown}"


    def venues(self):
        # Use the concerts relationship to get associated venues
        return [concert.venue for concert in self.concerts]
