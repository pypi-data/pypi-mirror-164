from arkdata.database.table import Table
from secrets import token_urlsafe
from pathlib import Path
from arkdata import models
from arkdata.seeds.data.cart_items import seed
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String


class CartItem(Table):
    __tablename__ = "cart_items"
    __type_name__ = "CART_ITEM"
    __sql_file__ = Table.__sql_file__ / Path("cart_items.sql")

    xuid = Column(String(100), nullable=False)
    product_id = Column(Integer, unique=True, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    @classmethod
    def seed(cls) -> None:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()

    @classmethod
    def purchase(cls, xuid: str) -> bool:
        account = models.Account.first(xuid=xuid)
        cost = cls.cart_total(xuid)
        if cost > account.berry_bush_seeds:
            return False
        order_id = token_urlsafe(16)
        cart = cls.where(xuid=xuid)
        for item in cart:
            models.OrderItem.new(
                xuid=item.xuid,
                product_id=item.product_id,
                quantity=item.quantity,
                order_id=order_id
            )
            item.delete()
        account.subtract_berries(cost)
        return True

    @classmethod
    def cart_total(cls, xuid: str) -> int:
        cart = cls.where(xuid=xuid)
        return sum([item.product.price for item in cart])

    @property
    def user(self) -> 'models.User':
        return models.User.first(xuid=self.xuid)

    @property
    def account(self) -> 'models.Account':
        return models.Account.first(xuid=self.xuid)

    @property
    def product(self) -> 'models.Product':
        return models.Product.first(id=self.product_id)

    def item(self):
        product = self.product
        return product.item()

    def update_quantity(self, quantity) -> None:
        self.update({'quantity': quantity}, id=self.id)

