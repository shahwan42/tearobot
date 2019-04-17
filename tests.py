import unittest
import time
import os
from pathlib import Path

from bot.commands import calculate, translate
from bot.db import DBHelper

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
        self.assertTrue(self.db.add_message((1, 2, 3, 4, 5, "message 1")))
        print("testing message insertion... done.")

    def test_add_user(self):
        self.assertTrue(self.db.add_user(
            (1, 0, 0, "user", "", "username1", "en", 1, time.time(), time.time(), "/start")
        ))


class CommandsTest(unittest.TestCase):

    def test_calculate_command(self):
        self.assertEqual(calculate("5*5"), "Result: 25")

    def test_translate_command(self):
        self.assertEqual(translate("Ahmed"), "أحمد")


if __name__ == "__main__":
    unittest.main()
