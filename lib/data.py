from models import State, County, City, Facilities, association_table as CityFacilityAssociation


states_to_add = [
    State(
        name="Alabama",
        abbreviation="AL",
        population=4903185,
        capital="Montgomery",
        area=52420,
    ),
    State(
        name="Florida",
        abbreviation="FL",
        population=21538187,
        capital="Tallahassee",
        area=65758,

    )
]


counties_to_add = [
    County(name='Miami-Dade', population=2763366, area=733, state_id=2),
    County(name='Broward', population=2003268, area=466, state_id=2),
    County(name='Palm Beach', population=1543809, area=760, state_id=2),
    County(name='Hillsborough', population=1528924, area=394, state_id=2),
    County(name='Jefferson', population=679599, area=429, state_id=1),
    County(name='Mobile', population=415355, area=474, state_id=1),
    County(name='Madison', population=404155, area=310, state_id=1),
    County(name='Baldwin', population=246617, area=614, state_id=1),
]

from faker import Faker
fake = Faker()
cities_to_add = [
    City(name='City1 of Miami-Dade', population=921122, area=244.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=1),
    City(name='City2 of Miami-Dade', population=921122, area=244.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=1),
    City(name='City3 of Miami-Dade', population=921122, area=244.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=1),

    City(name='City1 of Broward', population=13191, area=367.63,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=2),
    City(name='City2 of Broward', population=13191, area=367.63,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=2),
    City(name='City3 of Broward', population=13191, area=367.63,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=2),

    City(name='City1 of Palm Beach', population=514603, area=253.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=3),
    City(name='City2 of Palm Beach', population=514603, area=253.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=3),
    City(name='City3 of Palm Beach', population=514603, area=253.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=3),

    City(name='City1 of Hillsborough', population=509641, area=131.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=4),
    City(name='City2 of Hillsborough', population=509641, area=131.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=4),
    City(name='City3 of Hillsborough', population=509641, area=131.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=2, county_id=4),

    City(name='City1 of Jefferson', population=226533, area=143.00,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=5),
    City(name='City2 of Jefferson', population=226533, area=143.00,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=5),
    City(name='City3 of Jefferson', population=226533, area=143.00,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=5),

    City(name='City1 of Mobile', population=138451, area=158.00,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=6),
    City(name='City2 of Mobile', population=138451, area=158.00,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=6),
    City(name='City3 of Mobile', population=138451, area=158.00,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=6),

    City(name='City1 of Madison', population=134718, area=103.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=7),
    City(name='City2 of Madison', population=134718, area=103.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=7),
    City(name='City3 of Madison', population=134718, area=103.33,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=7),

    City(name='City1 of Baldwin', population=82205, area=204.67,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=8),
    City(name='City2 of Baldwin', population=82205, area=204.67,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=8),
    City(name='City3 of Baldwin', population=82205, area=204.67,
         latitude=fake.latitude(), longitude=fake.longitude(), state_id=1, county_id=8)
]


facilities_to_add = [
    Facilities(
        name="Public School",
        description="An educational institution for children aged 5-18",
        facility_type="Education",
    ),
    Facilities(
        name="Public Library",
        description="A facility where people can borrow books and access digital resources",
        facility_type="Education",
    ),
    Facilities(
        name="Public Hospital",
        description="A healthcare institution providing treatment with specialized medical and nursing staff",
        facility_type="Healthcare",
    )
]

association_to_add = [
    {"city_id": 1, "facility_id": 1},
    {"city_id": 1, "facility_id": 2},
    {"city_id": 1, "facility_id": 3},
    {"city_id": 2, "facility_id": 1},
    {"city_id": 2, "facility_id": 2},
    {"city_id": 2, "facility_id": 3},
    {"city_id": 3, "facility_id": 1},
    {"city_id": 3, "facility_id": 2},
    {"city_id": 3, "facility_id": 3},
    {"city_id": 4, "facility_id": 1},
    {"city_id": 4, "facility_id": 2},
    {"city_id": 4, "facility_id": 3},
    {"city_id": 5, "facility_id": 1},
    {"city_id": 5, "facility_id": 2},
    {"city_id": 5, "facility_id": 3},
    {"city_id": 6, "facility_id": 1},
    {"city_id": 6, "facility_id": 2},
    {"city_id": 6, "facility_id": 3},
    {"city_id": 7, "facility_id": 1},
    {"city_id": 7, "facility_id": 2},
    {"city_id": 7, "facility_id": 3},
    {"city_id": 8, "facility_id": 1},
    {"city_id": 8, "facility_id": 2},
    {"city_id": 8, "facility_id": 3},
    {"city_id": 9, "facility_id": 1},
    {"city_id": 9, "facility_id": 2},
    {"city_id": 9, "facility_id": 3},
    {"city_id": 10, "facility_id": 1},
    {"city_id": 10, "facility_id": 2},
    {"city_id": 10, "facility_id": 3},
    {"city_id": 11, "facility_id": 1},
    {"city_id": 11, "facility_id": 2},
    {"city_id": 11, "facility_id": 3},
    {"city_id": 12, "facility_id": 1},
    {"city_id": 12, "facility_id": 2},
    {"city_id": 12, "facility_id": 3},
    {"city_id": 13, "facility_id": 1},
    {"city_id": 13, "facility_id": 2},
    {"city_id": 13, "facility_id": 3},
    {"city_id": 14, "facility_id": 1},
    {"city_id": 14, "facility_id": 2},
    {"city_id": 14, "facility_id": 3},
    {"city_id": 15, "facility_id": 1},
    {"city_id": 15, "facility_id": 2},
    {"city_id": 15, "facility_id": 3},
    {"city_id": 16, "facility_id": 1},
    {"city_id": 16, "facility_id": 2},
    {"city_id": 16, "facility_id": 3},
    {"city_id": 17, "facility_id": 1},
    {"city_id": 17, "facility_id": 2},
    {"city_id": 17, "facility_id": 3},
    {"city_id": 18, "facility_id": 1},
    {"city_id": 18, "facility_id": 2},
    {"city_id": 18, "facility_id": 3},
    {"city_id": 19, "facility_id": 1},
    {"city_id": 19, "facility_id": 2},
    {"city_id": 19, "facility_id": 3},
    {"city_id": 20, "facility_id": 1},
    {"city_id": 20, "facility_id": 2},
    {"city_id": 20, "facility_id": 3},
    {"city_id": 21, "facility_id": 1},
    {"city_id": 21, "facility_id": 2},
    {"city_id": 21, "facility_id": 3},
    {"city_id": 22, "facility_id": 1},
    {"city_id": 22, "facility_id": 2},
    {"city_id": 22, "facility_id": 3},
    {"city_id": 23, "facility_id": 1},
    {"city_id": 23, "facility_id": 2},
    {"city_id": 23, "facility_id": 3},
    {"city_id": 24, "facility_id": 1},
    {"city_id": 24, "facility_id": 2},
    {"city_id": 24, "facility_id": 3},
]
