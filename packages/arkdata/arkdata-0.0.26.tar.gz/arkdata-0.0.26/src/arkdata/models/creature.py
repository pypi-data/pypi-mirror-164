from arkdata.database.table import Table
from pathlib import Path
from arkdata import models
from arkdata.seeds.data.creatures import seed
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text


class Creature(Table):
    __tablename__ = "creatures"
    __type_name__ = "CREATURE"
    __sql_file__ = Table.__sql_file__ / Path("creatures.sql")

    name = Column(String(100), unique=True, nullable=False)
    name_tag = Column(String(100), nullable=True, default=None)
    category = Column(String(100), nullable=True, default=None)
    entity_id = Column(String(100), nullable=True, default=None)
    blueprint = Column(String(200), nullable=True, default=None)
    small_image_url = Column(String(200), nullable=True, default=None)
    large_image_url = Column(String(200), nullable=True, default=None)
    description = Column(Text, nullable=True, default=None)
    url = Column(String(200), nullable=True, default=None)
    color_id = Column(Integer, nullable=True, default=None)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()

    def saddles(self):
        return models.Saddle.where(creature_name_tag=self.name_tag)

    def tek_saddle(self):
        return models.Saddle.first(creature_name_tag=self.name_tag, type='TEK')

    def saddle(self):
        return models.Saddle.first(creature_name_tag=self.name_tag, type='REGULAR')

    def platform_saddle(self):
        return models.Saddle.first(creature_name_tag=self.name_tag, type='PLATFORM')

