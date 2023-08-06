from arkdata import models


def seed():
    models.Server.new(name="GSG Server", map="ragnarok", xuid="123", address="127.0.0.1:5000")
