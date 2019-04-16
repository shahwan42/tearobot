import unittest
import time

from tbot.commands import calculate, translate
from tbot.db import DBHelper as db
from tbot import BASE_DIR

DB_FILE = BASE_DIR / 'db' / 'db.dev'
DB_SQL_SCRIPT = BASE_DIR / 'db' / 'bot.db.sql'


class DBHelperTest(unittest.TestCase):

    def setUp(self):
        """Create/connect to development database"""
        self.SQL_SCRIPT = DB_SQL_SCRIPT.read_text()  # read a PosixPath file as str
        # db connection & creation
        self.db = db(filename=str(DB_FILE))
        print("connecting to db... done.")
        self.db.conn.executescript(self.SQL_SCRIPT)
        self.db.conn.commit()
        print("creating tables... done.")

    def tearDown(self):
        """Drop DB tables, close connection and remove the db later"""
        self.db.conn.execute("DROP TABLE User;")
        self.db.conn.execute("DROP TABLE Message;")
        self.db.conn.commit()
        print("dropping tables... done.")
        self.db.conn.close()
        DB_FILE.unlink()  # PosixPath.unlink... remove a PosixPath file
        print("removing db file... done.")

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
