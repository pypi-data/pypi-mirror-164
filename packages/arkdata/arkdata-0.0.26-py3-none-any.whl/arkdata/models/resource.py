from arkdata.database.table import Table
from pathlib import Path
from arkdata.seeds.data.resources import seed
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String


class Resource(Table):
    __tablename__ = "resources"
    __type_name__ = "RESOURCE"
    __sql_file__ = Table.__sql_file__ / Path("resources.sql")

    name = Column(String(100), unique=True, nullable=False)
    stack_size = Column(Integer, nullable=True, default=None)
    class_name = Column(String(100), nullable=True, default=None)
    blueprint = Column(String(200), nullable=True, default=None)
    description = Column(String(100), nullable=True, default=None)
    image_url = Column(String(500), nullable=True, default=None)
    url = Column(String(500), nullable=True, default=None)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()
