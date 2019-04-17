"""
    Database management module
"""
import os
import sqlite3
from pathlib import Path

from sqlite3 import Error
from .data_types import User, Message

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "db")
DB_SQL_SCRIPT = os.path.join(BASE_DIR, "db", "bot.db.sql")


class DBHelper():

    def __init__(self, filename="bot.db"):
        try:
            self.db_file = str(os.path.join(DB_DIR, filename))
            self.conn = sqlite3.connect(self.db_file)  # new db connection
            self.cur = self.conn.cursor()  # obtain a cursor
        except Error as err:
            exit(err)

    def setup(self) -> bool:
        """Set up database for dev/test purpose or for first time use"""
        try:
            self.conn.executescript(Path(DB_SQL_SCRIPT).read_text())
            print("DB file path: " + self.db_file)
            print("DB setup was successful")
        except Error as err:
            exit(err)
        return True

    def destroy(self):
        try:
            self.conn.execute("DROP TABLE User;")
            self.conn.execute("DROP TABLE Message;")
            self.conn.commit()
            print("dropping tables... done.")
            self.conn.close()
            os.remove(self.db_file)
            print("removing db file... done.")
        except Error as err:
            exit(err)

    def query(self, sql: str, params: tuple):
        """Executes a custom query"""
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
        except Error as err:
            self.conn.rollback()
            exit(err)

    def add_message(self, params: tuple) -> bool:
        """Insert a new Message

        ``params`` tuple(``id``: int, ``update_id``: int, ``user_id``: int, ``chat_id``: int,
        ``date``: int(unix_timestamp), ``text``: str"""
        sql = "INSERT INTO Message VALUES (?, ?, ?, ?, ?, ?)"
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def get_message(self, message_id: int) -> Message or bool:
        """Retrieve message by its id"""
        sql = "SELECT * FROM Message WHERE id = ?"
        try:
            self.cur.execute(sql, (message_id,))
            rows = [row for row in self.cur.fetchall()]
            if len(rows) > 0:
                return Message(*rows[0])
            return False
        except Error as err:
            exit(err)

    def get_messages(self, user_id=None) -> list:
        """Retrieve messages for a certain user"""
        sql = "SELECT * FROM Message WHERE user_id = ?"
        try:
            result = self.cur.execute(sql, user_id)
            rows = [row for row in result]
        except Error as err:
            exit(err)
        return rows

    def add_user(self, params: tuple) -> bool:
        """Insert a new user

        ``params``: tuple(``id``: int, ``is_bot``: int, ``is_admin``: int, ``first_name``: str, ``last_name``: str,
        ``username``: str, ``language_code``: str, ``active``: int(0|1), ``created``: int(unix_timestamp),
        ``updated``: int(unix_timestamp), ``last_command``: str)"""
        sql = "INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def get_user(self, user_id: int) -> User:
        """Get a user object using ``user_id``"""
        sql = "SELECT * FROM User WHERE id = ?"
        user = None
        user_data = None
        try:
            result = self.cur.execute(sql, (user_id,))
            user_data = result.fetchall()
            print("getting user..", user_data)
            if len(user_data) > 0:
                user = User(*user_data[0])
            if user:
                return user
            return None
        except Error as err:
            exit(err)

    def set_user_last_command(self, user_id: int, updated: int, last_command: str):
        """Update user's last command"""
        try:
            sql = "UPDATE User SET updated = ?, last_command = ? WHERE id = ?"
            self.cur.execute(sql, (updated, last_command, user_id))
            self.conn.commit()
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def set_user_status(self, user_id: int, updated: int, active: bool):
        """Activate/deactivate a user"""
        status = 0
        if active:
            status = 1
        try:
            sql = "UPDATE User SET updated = ?, active = ? WHERE user_id = ?"
            self.cur.execute(sql, (updated, status, user_id))
            self.conn.commit()
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)
