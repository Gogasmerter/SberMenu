import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Dish(SqlAlchemyBase):
    __tablename__ = "dishes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "image": self.image,
        }

    orders = orm.relationship("DishOrder", back_populates="dish", lazy="dynamic")
    categories = orm.relationship("DishCategory", back_populates="dish", lazy="dynamic", cascade="all, delete-orphan")
