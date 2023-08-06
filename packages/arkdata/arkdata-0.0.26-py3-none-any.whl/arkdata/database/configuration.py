import os
from dotenv import dotenv_values
from collections import defaultdict


config = defaultdict(lambda: None)
config.update({
    **dotenv_values(".env.shared"),     # load shared development variables
    **dotenv_values(".env.secret"),     # load sensitive variables
    **os.environ,                       # override loaded values with environment variables
})

DATABASE_USERNAME = config['MYSQL_USERNAME'] or 'root'
DATABASE_PASSWORD = config['MYSQL_PASSWORD'] or 'password'

DATABASE_HOST = config['MYSQL_HOST'] or "127.0.0.1"
DATABASE_PORT = config['MYSQL_PORT'] or "3306"
DATABASE = config['MYSQL_DATABASE'] or "default_database"
DATABASE_URI = f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE}"

TEST_DATABASE_HOST = config['MYSQL_TEST_HOST'] or "127.0.0.1"
TEST_DATABASE_PORT = config['MYSQL_TEST_PORT'] or "3306"
TEST_DATABASE = config['MYSQL_TEST_DATABASE'] or "test_default_database"
TEST_DATABASE_URI = f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{TEST_DATABASE_HOST}:{TEST_DATABASE_PORT}/{TEST_DATABASE}"

