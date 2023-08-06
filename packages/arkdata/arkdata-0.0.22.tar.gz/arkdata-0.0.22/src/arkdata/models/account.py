from arkdata import models
from pathlib import Path
from arkdata.database.table import Table
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String


class Account(Table):
    __tablename__ = "accounts"
    __sql_file__ = Table.__sql_file__ / Path("accounts.sql")

    xuid = Column(String(100), nullable=False, unique=True)
    player_id = Column(Integer, nullable=True, default=None)
    player_name = Column(String(100), nullable=True, default=None)
    tribe_id = Column(Integer, nullable=True, default=None)
    tribe_name = Column(String(100), nullable=True, default=None)
    berry_bush_seeds = Column(Integer, nullable=False, default=0)
    influence_points = Column(Integer, nullable=False, default=0)
    nitrado_id = Column(String(100), nullable=True, default=None)
    server_id = Column(String(100), nullable=True, default=None)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        arkdata.seeds.data.accounts.seed()

    @staticmethod
    def server_wipe():
        Account.update({
            'player_id': None,
            'player_name': None,
            'tribe_id': None,
            'tribe_name': None,
            'berry_bush_seeds': 1000,
            'nitrado_id': None,
            'server_id': None,
        })
        # TODO: update server_id + 1

    @property
    def user(self):
        return models.User.first(xuid=self.xuid)

    def add_berries(self, berries: int):
        self.berry_bush_seeds += berries
        Account.update({'berry_bush_seeds': self.berry_bush_seeds}, xuid=self.xuid)
        return self

    def add_influence(self, points: int):
        self.influence_points += points
        Account.update({'influence_points': self.influence_points}, xuid=self.xuid)
        return self

    def subtract_berries(self, berries: int):
        self.berry_bush_seeds -= berries
        Account.update({'berry_bush_seeds': self.berry_bush_seeds}, xuid=self.xuid)
        return self

    def subtract_influence(self, points: int):
        self.influence_points -= points
        Account.update({'influence_points': self.influence_points}, xuid=self.xuid)
        return self

    def cart(self):
        return models.CartItem.where(xuid=self.xuid)

    def orders(self, **kwargs):
        return models.OrderItem.where(xuid=self.xuid, **kwargs)


if __name__ == '__main__':
    # make sure cwd is the root folder
    models.reset_all()

    Account()

    user = models.User.new(xuid='1234', gamertag="zed3kiah")
    print(user)
    models.User.update({'gamertag': 'Zed3kiah', 'berry_bush_seeds': 300})
    print(models.User.all())

    account = Account.new(xuid='1234', player_id=123456, player_name='zed', server_id=1)
    print(account)
    Account.update({'player_name': 'Zed3kiah'})
    print(Account.all())

