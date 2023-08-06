from pathlib import Path
from arkdata.database.table import Table
from arkdata import models
from arkdata.seeds.data.products import seed
# ProductType = Enum('CREATURE', name="ProductType")
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String


class Product(Table):
    __tablename__ = "products"
    __type_name__ = "PRODUCT"
    __sql_file__ = Table.__sql_file__ / Path("products.sql")

    name = Column(String(100), unique=False, nullable=False)
    price = Column(Integer, unique=False, nullable=True, default=65535)
    type = Column(String(100), unique=False, nullable=False)
    discount = Column(Integer, unique=False, nullable=False, default=0)
    #type = Column(ProductType, unique=False, nullable=False)
    #product_to_blueprint = relationship('ProductToBlueprint', backref='product', lazy=True)

# class ProductToBlueprint(Model):
#     __tablename__ = "product_to_blueprint"
#     product_id = id = Column(Integer, ForeignKey('product.id'), primary_key=True, nullable=False)
#     blueprint_id = Column(Integer, ForeignKey('blueprint.id'), unique=False, nullable=False)
#     blueprint = relationship('Blueprint', backref='product_to_blueprint', lazy=True)

    @classmethod
    def seed(cls):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} must exist to seed.")
        seed()

    def item(self):
        if self.type == 'CREATURE':
            return models.Creature.first(name=self.name)
        elif self.type == 'AMMUNITION':
            return models.Ammunition.first(name=self.name)
        elif self.type == 'ARMOUR':
            return models.Armour.first(name=self.name)
        elif self.type == 'ARTIFACT':
            return models.Artifact.first(name=self.name)
        elif self.type == 'ATTACHMENT':
            return models.Attachment.first(name=self.name)
        elif self.type == 'CART_ITEM':
            return models.CartItem.first(name=self.name)
        elif self.type == 'ORDER_ITEM':
            return models.OrderItem.first(name=self.name)
        elif self.type == 'CONSUMABLE':
            return models.Consumable.first(name=self.name)
        elif self.type == 'DYE':
            return models.Dye.first(name=self.name)
        elif self.type == 'EGG':
            return models.Egg.first(name=self.name)
        elif self.type == 'FARM':
            return models.Farm.first(name=self.name)
        elif self.type == 'RECIPE':
            return models.Recipe.first(name=self.name)
        elif self.type == 'RESOURCE':
            return models.Resource.first(name=self.name)
        elif self.type == 'SADDLE':
            return models.Saddle.first(name=self.name)
        elif self.type == 'SEED':
            return models.Seed.first(name=self.name)
        elif self.type == 'SKIN':
            return models.Skin.first(name=self.name)
        elif self.type == 'STRUCTURE':
            return models.Structure.first(name=self.name)
        elif self.type == 'TOOL':
            return models.Tool.first(name=self.name)
        elif self.type == 'TROPHY':
            return models.Trophy.first(name=self.name)
        elif self.type == 'WEAPON':
            return models.Weapon.first(name=self.name)


if __name__ == '__main__':
    # make sure cwd is the root folder
    Product.reset()
    item = Product.new(name='hatchet', type_id=1, type="CREATURE")
    print(item)
    Product.update({'name': 'new name'})
    print(Product.all())

