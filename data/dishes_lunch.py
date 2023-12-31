import sqlalchemy
from sqlalchemy import orm


from data.db_session import SqlAlchemyBase


class DishLunch(SqlAlchemyBase):
    __tablename__ = "dish_lunches"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    dish_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("dishes.id"))
    lunch_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("lunches.id"))
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("normalized_categories.id"), default=1)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=10)

    dish = orm.relationship("Dish", backref="lunches")
    lunch = orm.relationship("Lunch", back_populates="dishes")
    category = orm.relationship("NormalizedCategory", back_populates="lunch_dishes")
    orders = orm.relationship("DishLunchOrder", back_populates="dish", lazy="dynamic")
