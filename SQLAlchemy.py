from sqlalchemy import create_engine, String, Column
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker     
from sqlalchemy.engine import URL   # helps create line 24 URL object


base = declarative_base()

# Declare mapping class countries. Alternatively you can use any table from the mariaDB sample.
# Although you will have to edit the below class with the proper variables.
class countries(base):
    __tablename__ = "countries"
    country_id = Column(String,primary_key=True)
    name = Column(String)
    area = Column(String)
    national_day = Column(String)
    country_code2 = Column(String)
    country_code3 = Column(String)
    region_id = Column(String)

# Create your URL using the format here: 
# This is an alternate method of writing the database URL that I used
url_object = URL.create(
    "mysql",                
    username="root",        
    password="password",    # EDIT THIS LINE WITH YOUR MYSQL PASSWORD
    host="localhost",       
    database="nation",      
)

engine = create_engine(url_object)
factory = sessionmaker(bind=engine)
session = factory()

# IGNORE THIS, REFER TO THE END OF PROGRAM FOR WHY THIS BLOCK IS HERE
#deleted_country = session.query(countries).filter_by(name="Atlantis").first()
#session.delete(deleted_country)
#session.commit()

# Query method for Aruba, alternatively change the country name for a different country (i.e. Vietnam, Australia, etc.)
print("Query for Aruba:")
for instance in session.query(countries).filter_by(name="Aruba"):
    print("Country ID: ", instance.country_id)
    print("Name: ", instance.name)
    print("Area: ", instance.area)
    print("National Day: ", instance.national_day)
    print("Country Code: ", instance.country_code2)
    print("Alt. Country Code: ", instance.country_code3)
    print("Region ID: ", instance.region_id)
    print("---------")

    
# Execute method for United States, same as Query-- you can print any country via changing name
print("Execution for United States:")
countries_table = countries.metadata.tables["countries"]
for instance in session.execute(countries_table.select().where(countries_table.c.name == "United States")):
    print("Country ID: ", instance.country_id)
    print("Name: ", instance.name)
    print("Area: ", instance.area)
    print("National Day: ", instance.national_day)
    print("Country Code: ", instance.country_code2)
    print("Alt. Country Code: ", instance.country_code3)
    print("Region ID: ", instance.region_id)
    print("---------")

# Insert new country Atlantis, insert a sample country with every info inputted. It must NOT share a country code, name, 
# or id with another country in our database. I had to use the country code "AA" because "AS" or "AT" was taken
new_country = countries(country_id="240", name="Atlantis", area="3.3", national_day = "2000-10-10", country_code2="AA", country_code3="ATL", region_id="11")
session.add(new_country)
session.commit()

# Execute method for Atlantis to check if our country is now in the database
print("Execution for new country, Atlantis:")
countries_table = countries.metadata.tables["countries"]
for instance in session.execute(countries_table.select().where(countries_table.c.name == "Atlantis")):
    print("Country ID: ", instance.country_id)
    print("Name: ", instance.name)
    print("Area: ", instance.area)
    print("National Day: ", instance.national_day)
    print("Country Code: ", instance.country_code2)
    print("Alt. Country Code: ", instance.country_code3)
    print("Region ID: ", instance.region_id)
    print("---------")

# Update Atlantis with a new national day
updated_country = session.query(countries).filter_by(name="Atlantis").first()
updated_country.national_day = "2020-11-11"
session.commit()

# Check if national day was updated
print("Execution for updated country, Atlantis:")
countries_table = countries.metadata.tables["countries"]
for instance in session.execute(countries_table.select().where(countries_table.c.name == "Atlantis")):
    print("Country ID: ", instance.country_id)
    print("Name: ", instance.name)
    print("Area: ", instance.area)
    print("National Day: ", instance.national_day)
    print("Country Code: ", instance.country_code2)
    print("Alt. Country Code: ", instance.country_code3)
    print("Region ID: ", instance.region_id)
    print("---------")

# Delete Atlantis
deleted_country = session.query(countries).filter_by(name="Atlantis").first()
session.delete(deleted_country)
session.commit()

# IF you are testing, always have a delete method of any insertion.
# Why? Because if you insert a country or instance without deleting it, it is NOW in the database!
# Say I created Atlantis without this deletion block, next time I run it there will already be an Atlantis instance in the database.
# You can circumvent this easily however, by deleting the new instance very early on-- which is where the big comment block is in the
# beginning.