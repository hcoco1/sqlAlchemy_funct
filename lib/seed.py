import click
import time
import sys
import logging
from models import State, County, City, Facilities, association_table as CityFacilityAssociation, Base
from sqlalchemy.orm import sessionmaker
from geopy import exc as geopy_exc
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderUnavailable
from data import states_to_add, counties_to_add, cities_to_add, facilities_to_add, association_to_add
from sqlalchemy import create_engine
from sqlalchemy import or_, and_
from sqlalchemy import exc

user_agent_name = "GeoApp v1.0 (hcoco1@hotmail.com.com)"
geolocator = Nominatim(user_agent=user_agent_name)
logging.getLogger("geopy").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)

DATABASE_URL = "sqlite:///geodata.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    """Manage the database records."""
    pass

@cli.command()
def seed_states():
    """Seed states."""
    session.query(State).delete()
    session.commit()
    session.add_all(states_to_add)
    session.commit()
    click.echo("✅ Done seeding states!")


@cli.command()
def seed_counties():
    """Seed counties."""
    session.query(County).delete()
    session.commit()
    session.add_all(counties_to_add)
    session.commit()
    click.echo("✅ Done seeding counties!")


@cli.command()
def seed_cities():
    """Seed cities."""
    session.query(City).delete()
    session.commit()
    session.add_all(cities_to_add)
    session.commit()
    click.echo("✅ Done seeding cities!")

from sqlalchemy import and_, or_
from geopy.exc import GeocoderServiceError, GeocoderUnavailable
import time




@cli.command()
def seed_facilities():
    """Seed facilities."""
    session.query(Facilities).delete()
    session.commit()
    session.add_all(facilities_to_add)
    session.commit()
    click.echo("✅ Done seeding facilities!")


@cli.command()
def seed_associations():
    """Seed associations."""
    session.execute(CityFacilityAssociation.delete())  # Delete existing associations
    for association in association_to_add:
        session.execute(CityFacilityAssociation.insert().values(**association))
    session.commit()
    click.echo("✅ Done seeding associations!")

session.close()
if __name__ == '__main__':
    print("🌱 Seeding DB...")
    cli()

# To create Tables: python seed.py create-tables
# To seed states: python seed.py seed-states
# To seed counties: python seed.py seed-counties
# To seed cities: python seed.py seed-cities
# To seed facilities: python seed.py seed-facilities
# To seed associations: python seed.py seed-associations

