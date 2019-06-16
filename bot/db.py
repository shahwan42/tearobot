"""
    Database management module
"""
import os
import sys
import sqlite3
from pathlib import Path

from sqlite3 import Error
from .data_types import User, Message, ScheduleEntry, Announcement
from loggingconfigs import config_logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "db")
DB_SQL_SCRIPT = os.path.join(BASE_DIR, "db", "bot.db.m1.sql")
log = config_logger(__name__)


class DBHelper():

    def __init__(self, filename="bot.db"):
        try:
            self.db_file = str(os.path.join(DB_DIR, filename))
            self.conn = sqlite3.connect(self.db_file, check_same_thread=False)  # new db connection
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
            self.conn.execute("DROP TABLE Announcement;")
            self.conn.execute("DROP TABLE Schedule;")
            self.conn.commit()
            log.info("dropping tables... done.")
            self.conn.close()
            os.remove(self.db_file)
            log.info("removing db file... done.")
        except Error as err:
            exit(err)

    def add_message(self, message: Message) -> bool:
        """Insert a new Message

        ``params`` tuple(``id``: int, ``update_id``: int, ``user_id``: int, ``chat_id``: int,
        ``date``: int(unix_timestamp), ``text``: str"""
        sql = "INSERT INTO Message VALUES (?, ?, ?, ?, ?, ?)"
        params = (message.id, message.update_id, message.user_id, message.chat_id, message.date, message.text)
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
            log.debug("Message Content: " + message.text)
            log.info("Message Added with id: " + str(message.id))
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def get_message(self, message_id: int) -> Message:
        """Retrieve message by its id"""
        sql = "SELECT * FROM Message WHERE id = ?"
        try:
            self.cur.execute(sql, (message_id,))
            rows = [row for row in self.cur.fetchall()]
            if len(rows) > 0:
                msg = Message(*rows[0])
                log.debug("Message Content: " + str(msg.text))
                log.info("Message Retrieved with id: " + str(msg.id))
                return msg
            else:
                log.info("No Message with id: " + str(message_id))
                return None
        except Error as err:
            exit(err)

    def add_user(self, user: User) -> bool:
        """Insert a new user"""
        sql = "INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (user.id, user.is_bot, user.is_admin, user.first_name, user.last_name, user.username,
                  user.language_code, user.active, user.created, user.updated, user.last_command, user.chat_id)
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
        try:
            result = self.cur.execute(sql, (user_id,))
            fetched_data = result.fetchone()
            log.info("getting user with id: " + str(user_id))
            log.debug("User data: " + str(fetched_data))
            if isinstance(fetched_data, tuple):
                user = User(*fetched_data)
            if user:
                return user
            return None
        except Error as err:
            exit(err)

    def get_users(self) -> list:
        """Return list of all Users"""
        sql = "SELECT * FROM User"
        users_list = list()
        try:
            for user in self.cur.execute(sql).fetchall():
                users_list.append(User(*user))
            return users_list
        except Error as err:
            exit(err)

    def set_user_last_command(self, user_id: int, updated: int, last_command: str) -> bool:
        """Update user's last command"""
        sql = "UPDATE User SET updated = ?, last_command = ? WHERE id = ?"
        try:
            self.cur.execute(sql, (updated, last_command, user_id))
            self.conn.commit()
            log.info("last command updated for user ID: " + str(user_id) + " - current command: " + str(last_command))
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def set_user_status(self, user_id: int, updated: int, active: int) -> bool:
        """Activate/deactivate a user"""
        status = 0
        if active:
            status = 1
        sql = "UPDATE User SET updated = ?, active = ? WHERE id = ?"
        try:
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

    def set_user_chat_id(self, user_id: int, updated: int, chat_id: int) -> bool:
        """Set user's chat_id if not set (for old users)"""
        sql = "UPDATE User SET updated = ?, chat_id = ? WHERE id = ?"
        try:
            self.cur.execute(sql, (updated, chat_id, user_id))
            self.conn.commit()
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def get_schedule(self) -> list:
        """Fetch schedule data"""
        sql = "SELECT * FROM Schedule"
        schedule_entries = []
        try:
            result = self.cur.execute(sql)
            for entry in result.fetchall():
                schedule_entries.append(
                    ScheduleEntry(entry[1], entry[2], entry[3], entry[0]))
            return schedule_entries
        except Error as err:
            exit(err)

    def get_schedule_of(self, day: str) -> list:
        """Returns a list of tuples in form of ("time:strftime": "subject:str")"""
        sql = "SELECT time, subject FROM Schedule WHERE day = ?"
        schedule = []
        try:
            result = self.cur.execute(sql, (day,))
            for entry in result.fetchall():
                schedule.append(entry)
            return schedule
        except Error as err:
            print(err, file=sys.stderr)
            return []

    def add_announcement(self, ann: Announcement) -> bool:
        """Create new Announcement"""
        sql = "INSERT INTO Announcement (time, description, done) VALUES (?, ?, ?)"
        try:
            self.cur.execute(sql, (ann.time, ann.description, ann.done))
            return True
        except Error as err:
            self.conn.rollback()
            exit(err)

    def get_announcements(self) -> list:
        """Retrieve description and time field from Announcement"""
        sql = "SELECT * FROM Announcement"
        ann_list = list()
        try:
            result = self.cur.execute(sql)
            for ann in result.fetchall():
                ann_obj = Announcement(ann[1], ann[2], ann[3], ann[0])
                ann_list.append(ann_obj)
            return ann_list
        except Error as err:
            exit(err)

    def update_announcement(self, id: int, done: str):
        """Update ann.done"""
        values = ["once", "twice", "cancelled"]
        if done not in values:
            exit("You must provide a valid done value")
        sql = "UPDATE Announcement SET done = ? WHERE id = ?"
        try:
            result = self.cur.execute(sql, (done, id))
            return result
        except Error as err:
            self.conn.rollback()
            exit(err)
