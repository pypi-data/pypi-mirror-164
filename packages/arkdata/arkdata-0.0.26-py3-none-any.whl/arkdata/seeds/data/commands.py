from arkdata import models


def backup_seed():
    # Keep if need to reformat, change, or enhance
    models.Command.new(xuid='123', player_id="123", address="127.0.0.1:5000", code="cheat tp blue")
    models.Command.new(xuid='123', player_id="123", address="127.0.0.1:5000", code="cheat tp red")
    models.Command.new(xuid='123', player_id="123", address="127.0.0.1:5000", code="cheat tp green")
    models.Command.new(xuid='123', player_id="123", address="127.0.0.1:5000", code="cheat gcm")

    items = [item.to_json() for item in models.Command.all()]
    print(items)


def seed():
    items = [
        {
            'code': 'cheat tp blue',
            'xuid': '123',
            'operation': 'OTHER',
            'player_id': '123',
            'id': 5,
            'operation_id': None,
            'executed': False,
            'address': '127.0.0.1:5000'
        },
        {
            'code': 'cheat tp red',
            'xuid': '123',
            'operation': 'OTHER',
            'player_id': '123',
            'id': 10,
            'operation_id': None,
            'executed': False,
            'address': '127.0.0.1:5000'
        },
        {
            'code': 'cheat tp green',
            'xuid': '123',
            'operation': 'OTHER',
            'player_id': '123',
            'id': 11,
            'operation_id': None,
            'executed': False,
            'address': '127.0.0.1:5000'
        },
        {
            'code': 'cheat gcm',
            'xuid': '123',
            'operation': 'OTHER',
            'player_id': '123',
            'id': 12,
            'operation_id': None,
            'executed': False,
            'address': '127.0.0.1:5000'
        }
    ]
    models.Command.bulk_insert(items)
