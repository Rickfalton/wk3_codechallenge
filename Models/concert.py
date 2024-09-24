from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def __repr__(self):
        return f"Concert('{self.band.name}', '{self.venue.title}', '{self.date}')"
    
    def __str__(self):
        return f"Concert on {self.date} by {self.band.name} at {self.venue.title}, {self.venue.city}"

    def hometown_show(self):
        # Check if the concert is in the band's hometown
        return self.venue.city == self.band.hometown

    def introduction(self):
        # Provide an introduction message
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
