import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Lunch(SqlAlchemyBase):
    __tablename__ = "lunches"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.DATE, nullable=False, unique=True)

    dishes = orm.relationship("DishLunch", back_populates="lunch", cascade="all, delete-orphan")
    orders = orm.relationship("LunchOrder", cascade="all, delete-orphan")
