from arkdata import models


def seed():
    for user in models.User.all()[:3]:
        user.purchase()
