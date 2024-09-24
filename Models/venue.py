from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f"Venue('{self.title}', '{self.city}')"
    
    def __str__(self):
        return f"{self.title} in {self.city}"

    def bands(self):
        return [concert.band for concert in self.concerts]
