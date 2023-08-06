from arkdata.seeds.data import accounts
from arkdata.seeds.data import armours
from arkdata.seeds.data import artifacts
from arkdata.seeds.data import cart_items
from arkdata.seeds.data import consumables
from arkdata.seeds.data import commands
from arkdata.seeds.data import creatures
from arkdata.seeds.data import eggs
from arkdata.seeds.data import order_items
from arkdata.seeds.data import recipes, ammunitions, dyes, weapons, products, attachments, tools, users, farms, \
    skins
from arkdata.seeds.data import resources
from arkdata.seeds.data import saddles
from arkdata.seeds.data import seeds
from arkdata.seeds.data import structures
from arkdata.seeds.data import trophies
from arkdata.seeds.data import servers
import sys
__all__ = ['seed']


def seed():
    funcs = {
        'Armours': armours.seed,
        'Artifacts': artifacts.seed,
        'Attachments': attachments.seed,
        'Creatures': creatures.seed,
        'Consumables': consumables.seed,
        'Dyes': dyes.seed,
        'Eggs': eggs.seed,
        'Farms': farms.seed,
        'Recipes': recipes.seed,
        'Resources': resources.seed,
        'Saddles': saddles.seed,
        'Seeds': seeds.seed,
        'Skins': skins.seed,
        'Structures': structures.seed,
        'Tools': tools.seed,
        'Trophies': trophies.seed,
        'Weapons': weapons.seed,
        'Users': users.seed,
        'Accounts': accounts.seed,
        'Servers': servers.seed,
        'Commands': commands.seed,
        'Ammunitions': ammunitions.seed,
        'Products': products.seed,
        'Cart Items': cart_items.seed,
        'Order Items': order_items.seed,
        }
    for i, (name, func) in enumerate(funcs.items()):
        __printProgressBar(i, len(funcs), color='yellow', prefix="Seeding", suffix=name)
        func()
    __printProgressBar(1, 1, color='green', prefix='Seeding', suffix='Finished')


def __printProgressBar(iteration, total, prefix='', suffix='', color_temp=False, decimals=1, length=50, fill='█',
                     color=''):
    """
    Displays a progress bar for each iteration.
    Title: Progress Bar
    Author: Benjamin Cordier
    Date: 6/20/2019
    Availability: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    if sys.stdout.encoding != 'utf-8':
        return
    colors = {'': '30m', 'gray': '90m', 'red': '31m', 'green': '92m', 'yellow': '93m', 'purple': '35m',
              'orange': '33m', 'blue': '34m', 'pink': '95m', 'cyan': '96m', 'black': '97m', 'white': '38m'}
    if int(iteration % (total / 100)) == 0 or iteration == total or prefix != '' or suffix != '':
        # calculated percentage of completeness
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        # modifies the bar
        bar = fill * filledLength + '-' * (length - filledLength)
        # Creates the bar
        if color_temp:
            temp = {0.0: 'red', 35.0: 'orange', 65.0: 'yellow', 100.0: 'green'}
            color = temp[min([0.0, 35.0, 65.0, 100.0], key=lambda x: abs(x - float(percent)))]
        print(f'\r\r\033[{colors[color]}\t\t{prefix} |{bar}| {percent}% {suffix}{" " * 100}', end='\033[0m')
        # Print New Line on Complete
        if iteration == total:
            print()
