from app import app, db
from models import TypeBuilding, Country, City, Building

# with app.app_context():
    # types = [
    #     'Антенная мачта', 'Бетонная башня', 'Радиомачта',
    #     'Гиперболоидная башня', 'Дымовая труба', 'Решётчатая мачта',
    #     'Башня', 'Мост'
    # ]

    # items = [TypeBuilding(type_name) for type_name in types]

    # db.session.add_all(items)
    # db.session.commit()
    # print("Добавлено записей:", len(items))

with app.app_context():
    # query = TypeBuilding.query.all()
    # print(query)

    # query = TypeBuilding.query.filter(TypeBuilding.id == 5).all()
    # print(query)

    # query = TypeBuilding.query.filter(TypeBuilding.type_name.like("%мачта%")).all()
    # print(query)

    # query = (TypeBuilding.query.filter(TypeBuilding.type_name.like("%мачта%"))
    #     .order_by(TypeBuilding.type_name.desc()).all())
    # print(query)

    # query = TypeBuilding.query.filter(
    # (TypeBuilding.id > 3) & (TypeBuilding.type_name.like('%е%'))
    # ).all()
    # print(query)

    # TypeBuilding.query.filter(TypeBuilding.type_name == 'Мост')\
    #     .update({TypeBuilding.type_name: 'Мосты'})
    # db.session.commit()

    # query = TypeBuilding.query.all()
    # print(query)

    # TypeBuilding.query.filter(TypeBuilding.id == 8).delete()
    # db.session.commit()
    # query = TypeBuilding.query.all()
    # print(query)

    # countries = Country.query.all()
    # print("[")
    # for country in countries:
    #     print(f"  {country},")
    # print("]")

    cities = City.query.all()
    print("[")
    for city in cities:
        print(f"  {city},")
    print("]")

    buildings = Building.query.all()
    print("[")
    for b in buildings:
        print(f"  {b},")
    print("]")
