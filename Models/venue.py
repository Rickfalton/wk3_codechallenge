from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base
from Models.concert import Concert  
from Models.band import Band  

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

    def bands(self, session):
        """Returns bands that have performed at the venue using SQLAlchemy query."""
        return session.query(Band).join(Concert).filter(Concert.venue_id == self.id).all()
