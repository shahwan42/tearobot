import unittest
import time
import os
import sqlite3
from sqlite3 import Error
from pathlib import Path

from bot.commands import calculate, translate
from bot.db import DBHelper
from bot.data_types import Message

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_SQL_SCRIPT = os.path.join(BASE_DIR, "db", "bot.db.sql")


class DBHelperTest(unittest.TestCase):

    def setUp(self):
        """Create/connect to development database"""
        self.SQL_SCRIPT = Path(DB_SQL_SCRIPT).read_text()  # read a PosixPath file as str
        # db connection & creation
        self.db = DBHelper(filename="test.db")
        print("connecting to db... done.")
        self.db.setup()

    def tearDown(self):
        """Drop DB tables, close connection and remove the db later"""
        self.db.destroy()

    def test_add_message(self):
        # inserting the message
        msg = Message(1, 2, 3, 4, 5, "message 1")
        self.assertTrue(self.db.add_message(msg))
        # making sure it was inserted right
        sql = "SELECT * FROM Message"
        got_msg = Message(*self.db.cur.execute(sql).fetchone())
        self.assertEqual(msg.id, got_msg.id)
        self.assertEqual(msg.update_id, got_msg.update_id)
        self.assertEqual(msg.user_id, got_msg.user_id)
        self.assertEqual(msg.chat_id, got_msg.chat_id)
        self.assertEqual(msg.date, got_msg.date)
        self.assertEqual(msg.text, got_msg.text)
        print("testing message insertion... done.")

    def test_add_messages(self):
        pass

    def test_add_user(self):
        # TODO: use bare sql to test the returned result
        pass

    def test_add_users(self):
        """Test adding multiple users to the database"""
        pass

    def test_get_user(self):
        # TODO: first add the user using sql then get the user using the function
        # get user using sql and test the returned
        pass

    def test_get_users(self):
        # add users using sql, then get them using the function
        pass

    def test_set_user_last_command(self):
        # use the function to set, then use sql to test
        pass

    def test_set_user_status(self):
        pass

    def test_get_schedule(self):
        pass

    def test_get_events(self):
        pass


class CommandsTest(unittest.TestCase):

    def test_calculate_command(self):
        self.assertEqual(calculate("5*5"), "Result: 25")

    def test_translate_command(self):
        self.assertEqual(translate("Ahmed"), "أحمد")


if __name__ == "__main__":
    unittest.main()
