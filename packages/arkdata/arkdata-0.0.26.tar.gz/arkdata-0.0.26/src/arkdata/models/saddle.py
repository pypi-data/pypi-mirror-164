from arkdata.database.table import Table
from pathlib import Path
from arkdata.seeds.data.saddles import seed
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text


class Saddle(Table):
    __tablename__ = "saddles"
    __type_name__ = "SADDLE"
    __sql_file__ = Table.__sql_file__ / Path("saddles.sql")

    name = Column(String(100), unique=True, nullable=False)
    creature_name_tag = Column(String(100), unique=False, nullable=False)
    type = Column(String(100), nullable=False, default='OTHER')
    stack_size = Column(Integer, nullable=True, default=None)
    class_name = Column(String(100), nullable=True, default=None)
    blueprint = Column(String(200), nullable=True, default=None)
    description = Column(String(100), nullable=True, default=None)
    image_url = Column(String(500), nullable=True, default=None)
    summary = Column(Text, default=None)
    url = Column(String(500), nullable=True, default=None)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()
