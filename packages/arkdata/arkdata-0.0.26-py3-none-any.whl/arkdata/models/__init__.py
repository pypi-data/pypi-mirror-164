from arkdata.models.account import Account
# from models.admin import Admin
from arkdata.models.ammunition import Ammunition
from arkdata.models.armour import Armour
from arkdata.models.artifact import Artifact
from arkdata.models.attachment import Attachment
from arkdata.models.cart_item import CartItem
from arkdata.models.command import Command
from arkdata.models.consumable import Consumable
from arkdata.models.creature import Creature
from arkdata.models.dye import Dye
from arkdata.models.egg import Egg
from arkdata.models.farm import Farm
from arkdata.models.order_item import OrderItem
from arkdata.models.product import Product
from arkdata.models.recipe import Recipe
from arkdata.models.resource import Resource
from arkdata.models.saddle import Saddle
from arkdata.models.seed import Seed
from arkdata.models.skin import Skin
from arkdata.models.structure import Structure
from arkdata.models.tool import Tool
from arkdata.models.trophy import Trophy
from arkdata.models.user import User
from arkdata.models.weapon import Weapon
from arkdata.models.server import Server

__all__ = ['build_all', 'drop_all', 'reset_all']


def drop_all():
    models = [OrderItem, CartItem, Command, Server, Product, Account, User, Ammunition, Armour, Artifact, Attachment,
              Saddle, Consumable, Creature, Dye, Egg, Farm, Recipe, Resource,
              Seed, Skin, Structure, Tool, Trophy, Weapon]
    for i, model in enumerate(models):
        __progress_bar(i, len(models), color='red', prefix='Dropping', suffix=f'{model.__tablename__}')
        model.drop()
    __progress_bar(1, 1, color='green', prefix='Dropping', suffix='Finished')


def build_all():
    models = [User, Account, Product, OrderItem, CartItem, Server, Command, Ammunition, Armour, Artifact, Attachment,
              Consumable, Creature, Dye, Egg, Farm, Recipe, Resource, Saddle,
              Seed, Skin, Structure, Tool, Trophy, Weapon]
    for i, model in enumerate(models):
        __progress_bar(i, len(models), color='blue', prefix='Building', suffix=f"{model.__tablename__}")
        model.build()
    __progress_bar(1, 1, color='green', prefix='Building', suffix='Finished')


def clear_all():
    models = [User, Account, Product, OrderItem, CartItem, Command, Server, Ammunition, Armour, Artifact, Attachment,
              Consumable, Creature, Dye, Egg, Farm, Recipe, Resource, Saddle,
              Seed, Skin, Structure, Tool, Trophy, Weapon]
    for i, model in enumerate(models):
        __progress_bar(i, len(models), color='yellow', prefix=f"Clearing", suffix=f'{model.__tablename__}')
        model.clear()
    __progress_bar(1, 1, color='green', prefix='Clearing', suffix='Finished')


def reset_all():
    drop_all()
    build_all()


def __progress_bar(iteration, total, prefix='', suffix='', color_temp=False, decimals=1, length=50, fill='█',
                   color=''):
    """
    Displays a progress bar for each iteration.
    Title: Progress Bar
    Author: Benjamin Cordier
    Date: 6/20/2019
    Availability: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    colors = {'': '0', 'gray': '90', 'red': '31', 'green': '92', 'yellow': '93', 'purple': '35',
              'orange': '33', 'blue': '34', 'pink': '95', 'cyan': '96', 'black': '97', 'white': '38'}
    if int(iteration % (total / 100)) == 0 or iteration == total or prefix != '' or suffix != '':
        # calculated percentage of completeness
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        # modifies the bar
        bar = fill * filled_length + '-' * (length - filled_length)
        # Creates the bar
        if color_temp:
            temp = {0.0: 'red', 35.0: 'orange', 65.0: 'yellow', 100.0: 'green'}
            color = temp[min([0.0, 35.0, 65.0, 100.0], key=lambda x: abs(x - float(percent)))]
        bar_color = f"\033[{colors[color]}m"
        print(f'\r{bar_color}\t\t{prefix} |{bar}| {percent}% {suffix}{" " * 100}', end='\033[0m')
        # Print New Line on Complete
        if iteration == total:
            print()
