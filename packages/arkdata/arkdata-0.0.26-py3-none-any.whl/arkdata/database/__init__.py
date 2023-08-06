from arkdata.database.cusor import Cursor
from arkdata.database.table import Table
from arkdata.database.configuration import DATABASE_USERNAME, DATABASE_PASSWORD
from arkdata.database.configuration import DATABASE, DATABASE_HOST, DATABASE_PORT
from arkdata.database.configuration import TEST_DATABASE, TEST_DATABASE_HOST, TEST_DATABASE_PORT
from arkdata.database.configuration import TEST_DATABASE_URI, DATABASE_URI


def drop_all():
    with Cursor() as cursor:
        cursor.drop_database(DATABASE)
        cursor.drop_database(TEST_DATABASE)


__all__ = ['Cursor', 'drop_all']


