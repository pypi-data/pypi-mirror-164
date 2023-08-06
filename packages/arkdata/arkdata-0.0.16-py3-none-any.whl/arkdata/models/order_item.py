from arkdata.database.table import Table
from pathlib import Path
from datetime import datetime
from arkdata.seeds.data.order_items import seed
from arkdata import models
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Boolean


class OrderItem(Table):
    __tablename__ = "order_items"
    __type_name__ = "ORDER_ITEM"
    __sql_file__ = Table.__sql_file__ / Path("order_items.sql")

    xuid = Column(String(100), unique=True, nullable=False)
    order_id = Column(String(100), unique=True, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    delivered = Column(Boolean, nullable=False, default=False)
    date = Column(DateTime, nullable=False, default=datetime.now())

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()

    @property
    def product(self):
        return models.Product.first(id=self.product_id)

    @property
    def item(self):
        product = self.product
        return product.item()

    @property
    def user(self):
        return models.User.first(xuid=self.xuid)

    def deliver(self):
        return self.update({'delivered': True}, id=self.id)

