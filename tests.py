import unittest
import sys
import os

from tbot.commands import calculate, translate
from tbot.types import User
from tbot.db import DBHelper as db


class DBTest(unittest.TestCase):

    def setUp(self):
        """Create/connect to development database"""
        self.db_file = ('db/db.dev')
        self.sql_schema = []

        try:
            with open('db/bot.db.sql', 'r') as file:
                for line in file:
                    self.sql_schema.append(line)
                self.sql_schema = ''.join(self.sql_schema)
            print('reading db schema... done.')

        except IOError as err:
            print('failed to get sql schema', file=sys.stderr)
            print(err, file=sys.stderr)
            self.fail('Test could not begin')

        # db connection & creation
        self.db = db(filename=self.db_file)
        self.db.conn.executescript(self.sql_schema)
        self.db.conn.commit()
        print('connecting to db... done.')

    def tearDown(self):
        """Drop DB tables, close connection and remove the db later"""
        self.db.conn.execute('DROP TABLE User;')
        self.db.conn.execute('DROP TABLE Message;')
        self.db.conn.commit()
        print('dropping tables... done.')
        self.db.conn.close()
        os.remove(self.db_file)
        print('removed db file')


    def test_create_user(self):
        user = self.db.create(
            type='user',
            id=123456789,
            is_bot=False,
            is_admin=False,
            first_name='Ahmed',
            last_name='',
            username='',
            language_code='en',
            active=True,
            created=1555085968,
            updated=1555086998,
            last_command='/start'
        )
        self.assertTrue(isinstance(user, User), 'must create a User object populated by db values')
        self.assertTrue(user.id, 123456789)
        self.assertEqual(len(user), 1)

    def test_update_user(self):
        table = 'User'
        columns = ['active', 'is_admin']
        values = [False, True]
        result = self.db.update(table, columns, values)
        self.assertTrue(result)


class CommandsTest(unittest.TestCase):

    def test_calculate_command(self):
        self.assertEqual(calculate('5*5'), 'Result: 25')

    def test_translate_command(self):
        self.assertEqual(translate('Ahmed'), 'أحمد')


if __name__ == "__main__":
    unittest.main()
