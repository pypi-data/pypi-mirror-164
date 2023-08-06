from arkdata import models
import random


def seed():
    for i, user in enumerate(models.User.all()):
        models.CartItem.new(xuid=user.xuid, product_id=i + 1, quantity=random.randint(1, 10))
