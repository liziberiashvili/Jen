from pathlib import Path

import mysql.connector

from utils.ParserUtils import ParserUtils


class DatabaseUtils:
    path = Path("resources/data_base_config.json")
    host_name = ParserUtils.parse_json(path.absolute())["host"]
    user_name = ParserUtils.parse_json(path.absolute())["user"]
    password_parsed = ParserUtils.parse_json(path.absolute())["password"]

    __db_connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=password_parsed
    )

    @classmethod
    def select(cls, query):
        cursor = cls.__db_connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    @classmethod
    def execute(cls, query):
        cursor = cls.__db_connection.cursor()
        cursor.execute(query)
        cls.__db_connection.commit()
        return cursor.rowcount
