import csv
from app import app
from config import db
from models import Country, City, Building

def country_upload():
    with open("data/country.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = Country(item[0])
            db.session.add(new_entry)
        db.session.commit()
        print("Страны добавлены")
    
def city_upload():
    with open("data/city.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            city = City(row[0], int(row[1]))
            db.session.add(city)
        db.session.commit()
        print("Города добавлены")

def building_upload():
    with open("data/building.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            building = Building(
                row[0],         # Название
                int(row[1]),    # type_building_id
                int(row[2]),    # city_id
                int(row[3]),    # год
                float(row[4])     # высота
            )
            db.session.add(building)
        db.session.commit()
        print("Здания добавлены")

# with app.app_context():
    # country_upload()
    # city_upload()
    # building_upload()