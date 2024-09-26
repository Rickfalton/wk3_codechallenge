
# Concerts Project

## Overview
The Concerts Project is a database-driven application that defines and manages three main entities: **Band**, **Venue**, and **Concert**. It allows users to track performances by bands at various venues, providing insights into concert schedules and relationships.

### Key Entities
- **Band**: Represents a music band.
- **Venue**: Represents a concert venue.
- **Concert**: Represents a concert that occurs at a venue and features a band.

### Relationships
- A **Band** has many **Concerts**.
- A **Venue** has many **Concerts**.
- A **Concert** belongs to both a **Band** and a **Venue** (Many-to-Many relationship).

## Project Structure
```
Concerts/
├── Models/
│   ├── band.py         # Band model
│   ├── concert.py      # Concert model
│   └── venue.py        # Venue model
├── migrations/          # Alembic migrations folder
│   ├── env.py          # Environment setup for migrations
│   ├── versions/       # Folder for migration versions
│   └── alembic.ini     # Alembic configuration file
├── app.py               # Main entry point for running the app
├── config.py            # Config file for database and session setup
└── README.md            # This README file
```

## Setup Instructions
To set up the Concerts Project on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Rickfalton/wk3_codechallenge
   cd Concerts
   ```

2. **Install Dependencies**
   Ensure you have Python and pip installed. Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**
   Configure the database settings in `config.py`. Create the database if it doesn't exist.

4. **Run Migrations**
   To set up the database schema, run:
   ```bash
   alembic upgrade head
   ```

5. **Run the Application**
   Start the application with:
   ```bash
   python app.py
   ```

## Usage
Here are some examples of how to use the models in the application:

### Band Model
- **Create a Band**
  ```python
  from models.band import Band
  new_band = Band(name="The Rockers", hometown="Los Angeles")
  ```

- **Get Concerts for a Band**
  ```python
  concerts = new_band.concerts()
  ```

- **Play in a Venue**
  ```python
  new_band.play_in_venue(venue, "2024-10-01")
  ```

### Venue Model
- **Create a Venue**
  ```python
  from models.venue import Venue
  new_venue = Venue(title="The Grand Hall", city="New York")
  ```

- **Get Bands at a Venue**
  ```python
  bands = new_venue.bands()
  ```

### Concert Model
- **Get Band and Venue for a Concert**
  ```python
  concert_band = concert.band()
  concert_venue = concert.venue()
  ```

## Method Explanations

### Band Model Methods
- `concerts()`: Returns a list of all concerts the band has performed.
- `venues()`: Returns a list of all venues where the band has performed.
- `play_in_venue(venue, date)`: Creates a new concert for the band in the specified venue on the given date.
- `all_introductions()`: Returns a list of introductions for all concerts the band has played.
- `most_performances()`: Class method that returns the band with the most concerts.

### Venue Model Methods
- `concerts()`: Returns a list of all concerts at the venue.
- `bands()`: Returns a list of all bands that have performed at the venue.
- `concert_on(date)`: Finds and returns the concert at the venue on the specified date.
- `most_frequent_band()`: Returns the band that has performed the most at the venue.

### Concert Model Methods
- `band()`: Returns the band for the concert.
- `venue()`: Returns the venue for the concert.
- `hometown_show()`: Returns `True` if the concert is in the band’s hometown, `False` otherwise.
- `introduction()`: Returns a string introduction for the band at the concert.

## Additional Resources
- [Database Diagram](https://dbdiagram.io/d/sherehekubwa-66e87c016dde7f414947d4d1)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
