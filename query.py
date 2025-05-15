from app import app
from config import db
from models import Building, TypeBuilding, City, Country
from sqlalchemy import func, and_, select
from sqlalchemy.orm import joinedload

with app.app_context():

    print("1. Информация о каждом здании, отсортированная по убыванию высоты:")
    buildings = (db.session.query(
                    Building.title,
                    TypeBuilding.type_name.label('type'),
                    Country.name.label('country'),
                    City.name.label('city'),
                    Building.year,
                    Building.height
                )
                .join(TypeBuilding, Building.type_building_id == TypeBuilding.id)
                .join(City, Building.city_id == City.id)
                .join(Country, City.country_id == Country.id)
                .order_by(Building.height.desc())
                .all())

    for b in buildings:
        print(f"{b.title}, {b.type}, {b.country}, {b.city}, {b.year}, {b.height}")

    print("\n2. Макс, мин и средняя высота зданий в каждой стране, отсортировано по названию страны:")
    stats_by_country = (db.session.query(
                            Country.name,
                            func.max(Building.height),
                            func.min(Building.height),
                            func.avg(Building.height)
                        )
                        .join(City, City.country_id == Country.id)
                        .join(Building, Building.city_id == City.id)
                        .group_by(Country.id)
                        .order_by(Country.name)
                        .all())

    for s in stats_by_country:
        print(f"{s.name}: max={s[1]}, min={s[2]}, avg={round(s[3],2)}")

    print("\n3. Макс, мин и средняя высота зданий по каждому году, отсортировано по возрастанию года:")
    stats_by_year = (db.session.query(
                        Building.year,
                        func.max(Building.height),
                        func.min(Building.height),
                        func.avg(Building.height)
                    )
                    .group_by(Building.year)
                    .order_by(Building.year)
                    .all())

    for s in stats_by_year:
        print(f"{s.year}: max={s[1]}, min={s[2]}, avg={round(s[3],2)}")

    print("\n4. Макс, мин и средняя высота зданий для типов зданий, где в названии есть 'мачта', отсортировано по убыванию средней высоты:")
    stats_machta = (db.session.query(
                        TypeBuilding.type_name,
                        func.max(Building.height),
                        func.min(Building.height),
                        func.avg(Building.height)
                    )
                    .join(Building, Building.type_building_id == TypeBuilding.id)
                    .filter(TypeBuilding.type_name.ilike('%мачта%'))
                    .group_by(TypeBuilding.id)
                    .order_by(func.avg(Building.height).desc())
                    .all())

    for s in stats_machta:
        print(f"{s.type_name}: max={s[1]}, min={s[2]}, avg={round(s[3],2)}")

    print("\n5. Макс, мин и средняя высота зданий для стран с более чем одним зданием:")
    country_counts = (db.session.query(
                        Country.id
                    )
                    .join(City, City.country_id == Country.id)
                    .join(Building, Building.city_id == City.id)
                    .group_by(Country.id)
                    .having(func.count(Building.id) > 1)
                    ).subquery()

    stats_big_countries = (db.session.query(
                                Country.name,
                                func.max(Building.height),
                                func.min(Building.height),
                                func.avg(Building.height)
                            )
                            .join(City, City.country_id == Country.id)
                            .join(Building, Building.city_id == City.id)
                            .filter(Country.id.in_(select(country_counts)))
                            .group_by(Country.id)
                            .all())

    for s in stats_big_countries:
        print(f"{s.name}: max={s[1]}, min={s[2]}, avg={round(s[3],2)}")

