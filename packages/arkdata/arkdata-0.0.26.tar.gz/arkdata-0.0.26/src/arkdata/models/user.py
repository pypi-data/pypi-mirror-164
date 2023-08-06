from arkdata.database.table import Table
import bcrypt
from arkdata import models
from pathlib import Path
from secrets import token_urlsafe
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Boolean


class User(Table):
    __tablename__ = "users"
    __type_name__ = "USER"
    __sql_file__ = Table.__sql_file__ / Path("users.sql")

    xuid = Column(String(100), nullable=False, unique=True)
    gamertag = Column(String(100), unique=True, nullable=False)
    password_digest = Column(String(100), nullable=True, default=None)
    session_token = Column(String(100), nullable=True, default=None)
    authentication_token = Column(String(100), nullable=True, default=None)
    authenticated = Column(Boolean, default=False)
    discord_username = Column(String(100), default=None)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        arkdata.seeds.data.users.seed()

    @classmethod
    def new(cls, **values) -> 'Table':
        inputs = {k: v for k, v in values.items() if k != 'password'}
        if 'password' in values:
            # TODO: validate password size
            inputs['password_digest'] = bcrypt.hashpw(values['password'].encode(), bcrypt.gensalt()).decode()
        return super().new(**inputs)

    def logout(self) -> None:
        self.session_token = token_urlsafe(64)
        User.update({'session_token': self.session_token}, xuid=self.xuid)

    @property
    def accounts(self) -> list['models.Account']:
        return models.Account.where(xuid=self.xuid)

    def account(self, server_id: int) -> 'models.Account' or None:
        return models.Account.first(xuid=self.xuid, server_id=server_id)

    def cart(self) -> list['models.CartItem']:
        return models.CartItem.where(xuid=self.xuid)

    def orders(self, **kwargs) -> list['models.OrderItem']:
        return models.OrderItem.where(xuid=self.xuid, **kwargs)

    def add_to_cart(self, product: models.Product, quantity=1):
        return models.CartItem.new(xuid=self.xuid, product_id=product.id, quantity=quantity)

    def purchase(self):
        return models.CartItem.purchase(self.xuid)

    @staticmethod
    def authenticate_credentials(gamertag: str, password: str) -> 'User' or None:
        user = User.first(gamertag=gamertag)
        if user is None:
            return None
        if bcrypt.checkpw(password.encode(), user.password_digest.encode()):
            User.update({'session_token': token_urlsafe(64)}, xuid=user.xuid)
            return user

    @staticmethod
    def recovery(gamertag: str) -> None:
        user = User.first(gamertag=gamertag)
        if user:
            # TODO: send message to discord or xbox
            token = token_urlsafe(64)
            User.update({'authentication_token': token}, gamertag=gamertag)
            url = f"https://www.ark.com/recover/{token}"
            message = f"Click on the link to recover your user: {url}"

    @staticmethod
    def authenticate_recovery(authentication_token: str) -> 'User' or None:
        user = User.first(authentication_token=authentication_token)
        if user:
            user.authentication_token = token_urlsafe(64)
            user.authenticated = True
            User.update(user.to_json(), xuid=user.xuid)
            return user


if __name__ == "__main__":
    models.reset_all()
    user = User.new(xuid='1234', gamertag="zed3kiah")
    print(user)
    User.update({'gamertag': 'Zed3kiah'})
    print(User.all())
    user = models.Account.new(xuid='1234', player_id=123456, player_name='zed', server_id=1)
    print(user.user())
