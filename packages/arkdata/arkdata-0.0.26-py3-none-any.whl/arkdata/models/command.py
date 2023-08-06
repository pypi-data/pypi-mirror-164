from arkdata.database.table import Table
from pathlib import Path
from arkdata import models
from arkclient import APIClient
from arkdata.seeds.data.commands import seed
from arklibrary import Ini
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean


class Command(Table):
    __tablename__ = "commands"
    __type_name__ = "COMMAND"
    __sql_file__ = Table.__sql_file__ / Path("commands.sql")
    __max_batch_size__ = 10

    xuid = Column(String(100), unique=False, nullable=True)
    operation = Column(String, unique=False, nullable=False, default="OTHER")
    operation_id = Column(Integer, unique=False, nullable=True, default=None)
    code = Column(String, unique=False, nullable=False)
    executed = Column(Boolean, unique=False, nullable=False, default=False)

    # Admin's player id
    player_id = Column(String(100), unique=False, nullable=True, default=None)
    # Game Server IP Address or URL
    address = Column(String, unique=False, nullable=True, default=None)
    # Server id
    server_id = Column(Integer, unique=False, nullable=True, default=None)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()

    @classmethod
    def execute_all(cls):
        all = []
        commands = {}
        for command in cls.where(executed=False):
            all.append((command.code, command.address))
            commands[command.id] = {**command.to_json(), 'executed': True}
        if len(all):
            path = Path.cwd() / Path('config.ini')
            ini = Ini(path)
            host = ini['ARK-SERVER']['host']
            port = int(ini['ARK-SERVER']['port'])
            with APIClient(host=host, port=port) as connection:
                if not connection.connected:
                    return False
                code = '|'.join([code for code, address in all])
                server_id = 123
                connection.commands({'server_id': server_id, 'commands': [code]})
            cls.bulk_update(commands)
            return True

    @classmethod
    def executes(cls, **where):
        path = Path.cwd() / Path('config.ini')
        ini = Ini(path)
        host = ini['ARK-SERVER']['host']
        port = int(ini['ARK-SERVER']['port'])
        all = [command.code for command in cls.where(**where, executed=False)]
        if len(all):
            with APIClient(host=host, port=port) as connection:
                code = '|'.join(all)
                server_id = 123
                connection.commands({'server_id': server_id, 'commands': [code]})

    def server(self):
        return models.Server.first(id=self.server_id)

    def execute(self):
        if not self.executed:
            self.update({'executed': True}, id=self.id)
            path = Path.cwd() / Path('config.ini')
            ini = Ini(path)
            host = ini['ARK-SERVER']['host']
            port = int(ini['ARK-SERVER']['port'])
            with APIClient(host=host, port=port) as connection:
                server_id = 123
                connection.commands({'server_id': server_id, 'commands': [self.code]})
        else:
            print(f"Code already executed: {self.code}")

    def product(self):
        return models.Product.first(id=self.product_id)

    def user(self):
        return models.User.first(xuid=self.xuid)

