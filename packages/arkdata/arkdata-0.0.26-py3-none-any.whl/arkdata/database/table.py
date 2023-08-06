from arkdata.database.cusor import Cursor
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.orm import relationship
from pathlib import Path
import os
import arkdata


class Table:
    __table_args__ = {'extend_existing': True}
    __sql_file__ = None
    __database__ = None
    __host__ = None
    __port__ = None
    __sql_file__ = Path(os.path.dirname(arkdata.__file__)) / Path("seeds/tables")

    id = Column(Integer, nullable=False, primary_key=True)
    table = relationship('Table', backref='table')

    @classmethod
    def columns(cls):
        cols = []
        for key, val in cls.__dict__.items():
            if isinstance(val, Column):
                cols.append(key)
        for key, val in Table.__dict__.items():
            if isinstance(val, Column):
                cols.append(key)
        return cols

    @classmethod
    def all(cls) -> list:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        cursor = Cursor(database=cls.__database__)
        data = cursor.all(cls.__tablename__)
        items = [cls(**values) for values in data]
        return items

    @classmethod
    def first(cls, **where) -> 'Table':
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        cursor = Cursor(database=cls.__database__)
        data = cursor.first(cls.__tablename__, **where)
        if data:
            return cls(**data)

    @classmethod
    def length(cls) -> int:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        cursor = Cursor(database=cls.__database__)
        return cursor.length(cls.__tablename__)

    @classmethod
    def select(cls, **where) -> list:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        if len(where) == 0:
            return cls.all()
        return cls.where(**where)

    @classmethod
    def where(cls, **where) -> list:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        if len(where) == 0:
            raise Exception(f"Where parameters can not be empty.")
        cursor = Cursor(database=cls.__database__)
        data = cursor.find_by(cls.__tablename__, **where)
        return [cls(**values) for values in data]

    @classmethod
    def group_by(cls, keyfunc, **where):
        # TODO: add a group by
        # need execution to consoladate because
        # not all bots in the same server
        # e.g. group_by server_id
        pass

    @classmethod
    def new(cls, **values):
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        cols = cls.columns()
        kwargs = {k: v for k, v in values.items() if k in cols}
        cursor = Cursor(database=cls.__database__)
        cursor.insert(cls.__tablename__, **kwargs)
        if 'id' in values:
            return cls.first(id=values['id'])
        else:
            query = f"""SELECT * FROM {cls.__tablename__} WHERE id = (SELECT LAST_INSERT_ID())"""
            data = cursor.db.execute(query).mappings().first()
            if data:
                return cls(**data)

    @classmethod
    def bulk_insert(cls, values: list[dict]) -> bool:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        if len(values) == 0:
            return True
        arg_names = [name for name in values[0].keys()]
        cursor = Cursor(database=cls.__database__)
        cursor.bulk_insert(cls.__tablename__, arg_names, values)

    @classmethod
    def update(cls, values: dict, **where) -> None:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        cols = cls.columns()
        kwargs = {k: v for k, v in values.items() if k in cols}
        cursor = Cursor(database=cls.__database__)
        cursor.update(cls.__tablename__, kwargs, **where)

    @classmethod
    def bulk_update(cls, values: dict[dict]) -> None:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        if len(values) == 0:
            return
        all_values = {}
        cols = cls.columns()
        for item_id, val in values.items():
            all_values[item_id] = {k: v for k, v in val.items() if k in cols}
        cursor = Cursor(database=cls.__database__)

        cursor.bulk_update(cls.__tablename__, all_values)

    @classmethod
    def remove(cls, **where) -> None:
        if not cls.exists():
            raise Exception(f"Table {cls.__tablename__} does not exist.")
        cursor = Cursor(database=cls.__database__)
        cursor.remove(cls.__tablename__, **where)

    @classmethod
    def exists(cls, **where) -> bool:
        cursor = Cursor(database=cls.__database__)
        if not cursor.exists_database(cls.__database__):
            return False
        if len(where) == 0:
            return cursor.exists_table(cls.__tablename__)
        else:
            return cursor.exists(cls.__tablename__, **where)

    @classmethod
    def drop(cls) -> bool:
        if cls.exists():
            cursor = Cursor(database=cls.__database__)
            cursor.drop_table(cls.__tablename__)
        return not cls.exists()

    @classmethod
    def build(cls) -> bool:
        if cls.exists():
            return False
        cursor = Cursor(database=cls.__database__)
        if not cursor.exists_database():
            cursor.create_database()
        with open(cls.__sql_file__, 'r') as input_file:
            sql_text = input_file.read()
            cursor.db.execute(sql_text)
        return cls.exists()

    @classmethod
    def clear(cls) -> bool:
        if not cls.exists():
            return False
        if cls.length() == 0:
            return True
        cursor = Cursor(database=cls.__database__)
        cursor.clear_table(cls.__tablename__)
        return cls.length() == 0

    def __init__(self, **values):
        cols = self.columns()
        kwargs = {k: v for k, v in values.items() if k in cols}
        self.__dict__.update(**kwargs)

    def reload(self) -> None:
        item = self.first(id=self.id)
        for k, v in self.__dict__.items():
            self.__dict__[k] = item.__dict__[k]

    def delete(self) -> None:
        cursor = Cursor(database=self.__database__)
        cursor.remove(self.__tablename__, id=self.id)

    def to_json(self) -> dict:
        cols = self.columns()
        attrs = {k: v for k, v in self.__dict__.items() if k in cols}
        return attrs

    def __repr__(self):
        table_name = self.__tablename__.title().replace("_", "")
        items = []
        for k, v in self.to_json().items():
            items.append(f"\033[34m{k}\033[90m=\033[0m{repr(v)}\033[0m")
        args = ', '.join(items)
        return f'<\033[96m{table_name}\033[0m({args})>\033[0m'

    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        this_attrs = self.to_json()
        other_attrs = other.to_json()
        if len(this_attrs) != len(other_attrs):
            return False

        return all([k in other_attrs and v == other_attrs[k] for k, v in this_attrs.items()])



