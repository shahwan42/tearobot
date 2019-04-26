import unittest
import time
import os
from pathlib import Path

from bot.commands import calculate, translate
from bot.db import DBHelper
from bot.data_types import Message, User

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
        print("testing add_message... done.")

    def test_get_message(self):
        # inserting the message
        sql = "INSERT INTO Message VALUES (?, ?, ?, ?, ?, ?)"
        params = (1, 2, 3, 4, 5, "message")
        self.db.cur.execute(sql, params)
        # making sure we get it right
        msg = self.db.get_message(1)
        self.assertTrue(isinstance(msg, Message))
        self.assertEqual(msg.id, params[0])
        self.assertEqual(msg.update_id, params[1])
        self.assertEqual(msg.user_id, params[2])
        self.assertEqual(msg.chat_id, params[3])
        self.assertEqual(msg.date, params[4])
        self.assertEqual(msg.text, params[5])
        not_msg = self.db.get_message(2)
        self.assertFalse(not_msg)
        print("testing get_message... done.")

    def test_add_user(self):
        # insert new user
        user = User(70437390, False, True, "Ahmed", "Shahwan", "ash753", "en", True, 1555512911.45624,
                    1556303495.79887, "/calculate")
        self.assertTrue(self.db.add_user(user))
        # testing if it's inserted correctly
        sql = "SELECT * FROM User"
        got_user = User(*self.db.cur.execute(sql).fetchone())
        self.assertEqual(user.id, got_user.id)
        self.assertEqual(user.is_bot, got_user.is_bot)
        self.assertEqual(user.is_admin, got_user.is_admin)
        self.assertEqual(user.first_name, got_user.first_name)
        self.assertEqual(user.last_name, got_user.last_name)
        self.assertEqual(user.username, got_user.username)
        self.assertEqual(user.language_code, got_user.language_code)
        self.assertEqual(user.active, got_user.active)
        self.assertEqual(user.created, got_user.created)
        self.assertEqual(user.updated, got_user.updated)
        self.assertEqual(user.last_command, got_user.last_command)

    def test_get_user(self):
        # inserting user to db using sql
        sql = "INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (70437390, False, True, "Ahmed", "Shahwan", "ash753", "en", True, 1555512911.45624,
                  1556303495.79887, "/calculate")
        self.db.cur.execute(sql, params)
        # user exists
        user = self.db.get_user(params[0])
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.id, params[0])
        self.assertEqual(user.is_bot, params[1])
        self.assertEqual(user.is_admin, params[2])
        self.assertEqual(user.first_name, params[3])
        self.assertEqual(user.last_name, params[4])
        self.assertEqual(user.username, params[5])
        self.assertEqual(user.language_code, params[6])
        self.assertEqual(user.active, params[7])
        self.assertEqual(user.created, params[8])
        self.assertEqual(user.updated, params[9])
        self.assertEqual(user.last_command, params[10])
        # user doesn't exist
        not_user = self.db.get_user(111)
        self.assertTrue(not_user is None)

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
