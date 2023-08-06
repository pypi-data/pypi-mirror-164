from sqlalchemy import create_engine
from arkdata.database.configuration import DATABASE, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT


class Cursor:
    __int_types = {'bit', 'tinyint', 'smallint', 'mediumint', 'int', 'bigint'}
    __float_types = {'float', 'double', 'decimal'}
    __str_types = {'tinytext', 'text', 'blob', 'mediumtext', 'mediumblob', 'longtext',
                   'longblob', 'varchar', 'set', 'enum'}
    __datetime_types = {'date', 'datetime', 'timestamp', 'time', 'year'}
    is_types = {type(None)}

    def __init__(self, uri: str=None, database: str=None, host:str=None, port:str=None, username:str=None, password:str=None):
        if uri:
            credential_index = uri.index('@')
            self.username, password = uri[uri.index("//") + 2:credential_index].split(':')
            self.address, self.database = uri[credential_index + 1:].split('/')
        else:
            self.username = username or DATABASE_USERNAME
            password = password or DATABASE_PASSWORD
            self.address = f"{host or DATABASE_HOST}:{port or DATABASE_PORT}"
            self.database =database or  DATABASE

        self.db = create_engine(f"mysql://{self.username}:{password}@{self.address}")
        if not self.exists_database(self.database):
            self.create_database(self.database)
        self.use(self.database)

    def tables(self) -> list[str]:
        tables = self.db.execute(f"SHOW TABLES FROM {DATABASE}").all()
        return [table[0] for table in tables]

    def use(self, database: str):
        self.db.execute(f"USE {database}")

    def first(self, table: str, **where):
        query = f"""SELECT * FROM {table} LIMIT 1"""
        if len(where) == 0:
            return self.db.execute(query).mappings().first()
        where_str = self.where(**where)
        query = f"""SELECT * FROM {table} {where_str} LIMIT 1"""
        params = tuple(where.values())
        return self.db.execute(query, params).mappings().first()

    def is_empty(self):
        return len(self) == 0

    def bulk_insert(self, table: str, arg_names: list, values: list[dict]) -> None:
        if len(values) == 0:
            return
        formatted_names = ', '.join(arg_names)
        query = f"""\n\tINSERT INTO {table}\n\t({formatted_names})\n\tVALUES\n\t\t"""
        query += ',\n\t\t'.join(["(" + ','.join(["%s"] * len(arg_names)) + ")"] * len(values))
        all_values = [v for item in values for v in item.values()]
        self.db.execute(query, *all_values)

    def bulk_update(self, table: str, values: dict[dict]):
        if len(values) == 0:
            return
        first: dict = next(iter(values.values()))
        arg_names = first.keys()
        if 'id' not in arg_names:
            arg_names = ['id'] + list(arg_names)
        all_values = [{'id': item_id, **val} for item_id, val in values.items()]
        str_values = []
        for item in all_values:
            values = f"({','.join(['NULL' if v is None else repr(v) for v in item.values()])})"
            str_values.append(values)
        updates = ', '.join([f"{name} = VALUES({name})" for name in arg_names if name != 'id'])
        all_values_str = ',\n\t\t'.join(str_values)
        query = f"""INSERT INTO {table} ({','.join(arg_names)})
        VALUES
        {all_values_str}
        ON DUPLICATE KEY UPDATE {updates}"""
        self.db.execute(query)

    def where(self, **kwargs) -> str:
        comparator = [f"{k} is %s" if type(v) in self.is_types else f"{k} = %s" for k, v in kwargs.items()]
        arguments = ' and '.join(comparator)
        return f"WHERE {arguments}" if arguments else ''

    def all(self, table: str):
        query = f"""SELECT * FROM {table}"""
        return self.db.execute(query).mappings().all()

    def find_by(self, table: str, **where):
        where_str = self.where(**where)
        query = f"""SELECT * FROM {table} {where_str}"""
        params = tuple(where.values())
        return self.db.execute(query, params).mappings().all()

    def find_by_ignorecase(self, table: str, **where):
        assert len(where) > 0, "Where arguments must be provided."
        where_str = ' and '.join([f"UPPER({k}) = UPPER(%s)" for k in where.keys()])
        query = f"""SELECT * FROM {table} WHERE {where_str}"""
        params = tuple(where.values())
        return self.db.execute(query, params).mappings().all()

    def insert(self, table: str, **values):
        assert len(values) > 0, "Arguments for insert must be provided."
        query = f"""INSERT INTO {table} ({','.join(values.keys())})
                    VALUES ({','.join(['%s'] * len(values))})"""
        params = tuple(values.values())
        self.db.execute(query, params)

    def update(self, table: str, data, **where):
        assert len(data) > 0, "Data arguments for update must be provided."
        upd = ', '.join([f"{k} = %s" for k in data.keys()])
        where_str = self.where(**where)
        query = f"""UPDATE {table} SET {upd} {where_str}"""
        params = tuple(data.values()) + tuple(where.values())
        self.db.execute(query, params)

    def remove(self, table: str, **where):
        assert len(where) > 0, "A where statement must be provided"
        where_str = self.where(**where)
        query = f"""DELETE FROM {table} {where_str}"""
        params = tuple(where.values())
        self.db.execute(query, params)

    def exists(self, table: str, **where):
        params = self.where(**where)
        query = f"""SELECT COUNT(*) FROM {table} {params}"""
        params = tuple(where.values())
        data = self.db.execute(query, params).all()
        return data[0][0] > 0

    def exists_ignorecase(self, table: str, **where):
        assert len(where) > 0, "Where arguments must be provided."
        where_str = ' and '.join([f"UPPER({k}) = UPPER(%s)" for k in where.keys()])
        query = f"""SELECT COUNT(*) AS length FROM {table} WHERE {where_str}"""
        params = tuple(where.values())
        data = self.db.execute(query, params).all()
        return data[0][0] > 0

    def select_ignorecase(self, table: str, **where):
        assert len(where) > 0, "Where arguments must be provided."
        where_str = ' and '.join([f"UPPER({k}) = UPPER(%s)" for k in where.keys()])
        query = f"""SELECT * FROM {table} WHERE {where_str}"""
        params = tuple(where.values())
        return self.db.execute(query, params).mappings().all()

    def call_procedure(self, procedure, *args):
        args_str = ', '.join(['%s' for i in range(len(args))])
        data = self.db.execute(f"CALL {procedure}({args_str})", *args).mappings().all()
        return data

    def drop_procedure(self, procedure: str) -> None:
        self.db.execute(f"DROP PROCEDURE IF EXISTS {procedure}")

    def drop_database(self, database: str = None) -> None:
        self.db.execute(f"DROP DATABASE IF EXISTS {database or self.database}")

    def drop_table(self, table: str) -> None:
        self.db.execute(f"DROP TABLE IF EXISTS {table}")

    def create_database(self, database: str = None) -> None:
        self.db.execute(f"CREATE DATABASE IF NOT EXISTS {database or self.database}")

    def exists_database(self, database: str = None) -> bool:
        data = self.db.execute(f"""
        SELECT count(SCHEMA_NAME)
        FROM information_schema.SCHEMATA
        WHERE SCHEMA_NAME = '{database or self.database}'
        """).all()
        return data[0][0] > 0

    def exists_table(self, table: str) -> bool:
        data = self.db.execute(f"""
        SELECT COUNT(*) FROM information_schema.TABLES
        WHERE TABLE_SCHEMA = '{self.database}' AND TABLE_NAME = '{table}'
        """).all()
        return data[0][0] > 0

    def length(self, table: str) -> int:
        data = self.db.execute(f"SELECT COUNT(*) AS length FROM {table}").all()
        if len(data) == 0:
            return 0
        return data[0][0]

    def clear_table(self, table: str) -> None:
        if self.database == DATABASE:
            self.table_delete_all(table)
        else:
            self.table_truncate(table)

    def table_truncate(self, table: str) -> None:
        self.db.execute("SET FOREIGN_KEY_CHECKS = 0")
        self.db.execute(f"TRUNCATE {table}")
        self.db.execute(f"SET FOREIGN_KEY_CHECKS = 1")

    def table_delete_all(self, table: str) -> None:
        self.db.execute(f"DELETE FROM {table}")
        self.db.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1")

    def __len__(self):
        data = self.db.execute(f"""
        SELECT count(*) AS length
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = '{DATABASE}'
        """).all()
        if len(data) == 0:
            return 0
        return data[0][0]

    def __repr__(self):
        database = self.database
        address = self.address
        return f"<Cursor({database=}, {address=})>"
