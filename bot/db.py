"""
    Database management module
"""
import os
import sqlite3
from pathlib import Path

from sqlite3 import Error
from .data_types import User, Message
from loggingconfigs import config_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "db")
DB_SQL_SCRIPT = os.path.join(BASE_DIR, "db", "bot.db.sql")
log = config_logger(__name__)


class DBHelper():

    def __init__(self, filename="bot.db"):
        try:
            self.db_file = str(os.path.join(DB_DIR, filename))
            self.conn = sqlite3.connect(self.db_file)  # new db connection
            self.cur = self.conn.cursor()  # obtain a cursor
            log.info("DB Initialized.")
        except Error as err:
            exit(err)

    def setup(self) -> bool:
        """Set up database for dev/test purpose or for first time use"""
        try:
            self.conn.executescript(Path(DB_SQL_SCRIPT).read_text())
            log.debug("DB file path: " + self.db_file)
            log.info("DB setup was successful.")
        except Error as err:
            exit(err)
        return True

    def destroy(self):
        try:
            self.conn.execute("DROP TABLE User;")
            self.conn.execute("DROP TABLE Message;")
            self.conn.commit()
            log.info("dropping tables... done.")
            self.conn.close()
            os.remove(self.db_file)
            log.info("removing db file... done.")
        except Error as err:
            exit(err)

    def query(self, sql: str, params: tuple):
        """Executes a custom query"""
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
            log("Query Executed.")
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
            log.debug("Message Content: " + str(params))
            log.info("Message Added with id: " + str(params[0]))
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
                msg = Message(*rows[0])
                msg_content = (msg.id, msg.update_id, msg.user_id, msg.chat_id, msg.date, msg.text)
                log.debug("Message Content: " + str(msg_content))
                log.info("Message Retrieved with id: " + str(msg.id))
                return msg
            else:
                log.info("No Message with id: " + str(message_id))
                return False
        except Error as err:
            exit(err)

    def get_messages(self, user_id=None) -> list:
        """Retrieve messages for a certain user"""
        sql = "SELECT * FROM Message WHERE user_id = ?"
        try:
            result = self.cur.execute(sql, user_id)
            rows = [row for row in result]
            log.info("Messages Retrieved from user: " + str(user_id))
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
            log.debug("User data:" + str(params))
            log.info("adding new user... done")
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
            log.info("getting user with id: " + str(user_id))
            log.debug("User data: " + str(user_data))
            if len(user_data) > 0:
                user = User(*user_data[0])
            if user:
                return user
            return None
        except Error as err:
            exit(err)

    def get_events(self) -> list:
        """Retrieve description and time field from events"""
        sql = "SELECT description, time FROM Event"
        try:
            result = self.cur.execute(sql)
            rows = [row for row in result]
        except Error as err:
            exit(err)
        return rows

    def set_user_last_command(self, user_id: int, updated: int, last_command: str):
        """Update user's last command"""
        try:
            sql = "UPDATE User SET updated = ?, last_command = ? WHERE id = ?"
            self.cur.execute(sql, (updated, last_command, user_id))
            self.conn.commit()
            log.info("last command updated for user ID: " + str(user_id) + " - current command: " + str(last_command))
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def set_user_status(self, user_id: int, updated: int, active: int):
        """Activate/deactivate a user"""
        status = 0
        if active:
            status = 1
        try:
            sql = "UPDATE User SET updated = ?, active = ? WHERE id = ?"
            self.cur.execute(sql, (updated, status, user_id))
            self.conn.commit()
            if status:
                log.info("User: " + str(user_id) + " is activated.")
            else:
                log.info("User: " + str(user_id) + " is deactivated.")
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def get_schedule(self) -> list:
        """Fetch schedule data"""
        try:
            sql = "SELECT * FROM Schedule"
            result = self.cur.execute(sql)
            rows = [row for row in result]
            return rows
        except Error as err:
            exit(err)
