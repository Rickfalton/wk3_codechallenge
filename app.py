from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.base import Base
from Models.band import Band
from Models.venue import Venue
from Models.concert import Concert

# Create the engine
engine = create_engine('sqlite:///models/concerts.db')

# Create all tables
Base.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Band, Venue, and Concert
band = Band(name="The Rolling Stones", hometown="London")
venue1 = Venue(title="Wembley Stadium", city="London")
venue2 = Venue(title="Madison Square Garden", city="New York")

concert1 = Concert(date="2024-07-15", band=band, venue=venue1)
concert2 = Concert(date="2024-08-20", band=band, venue=venue2)

# Add them to the session
session.add(band)
session.add(venue1)
session.add(venue2)
session.add(concert1)
session.add(concert2)

# Commit the session
session.commit()

# Query the database and print the details
band = session.query(Band).first()
print(f'The band goes by the name: {band.name}')

# Get all concerts of the band
for concert in band.concerts:
    print(f"Concert on {concert.date} at {concert.venue.title}, {concert.venue.city}")

# List venues where the band has performed
print(band.venues())

# Show an introduction for the first concert
print(concert1.introduction())
