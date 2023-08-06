from arkdata.database.table import Table
from pathlib import Path
from arkdata import models
from sqlalchemy.schema import Column
from sqlalchemy.types import String


class Server(Table):
    __tablename__ = "servers"
    __type_name__ = "SERVER"
    __sql_file__ = Table.__sql_file__ / Path("servers.sql")
    __max_batch_size__ = 10

    name = Column(String, unique=False, nullable=False, default="UNKNOWN")
    xuid = Column(String(100), unique=True, nullable=True, default=None)
    player_id = Column(String, unique=False, nullable=True, default=None)
    nitrado_id = Column(String, unique=False, nullable=True, default=None)
    map = Column(String, unique=False, nullable=True, default=None)
    address = Column(String, unique=False, nullable=False)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        arkdata.seeds.data.servers.seed()

    def account(self):
        return models.Account.first(id=self.bot_xuid)

    def user(self):
        return models.User.first(xuid=self.xuid)

    def commands(self):
        return models.Command.where(server_id=self.id)

