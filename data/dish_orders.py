import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class DishOrder(SqlAlchemyBase):
    __tablename__ = "dish_orders"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    dish_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("dishes.id"))
    order_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("orders.id"))
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    dish = orm.relationship("Dish", back_populates="orders")
    order = orm.relationship("Order", back_populates="dishes")
