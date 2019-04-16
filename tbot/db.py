"""
    Database management module
"""
import os
import sqlite3

from sqlite3 import Error


class DBHelper():

    def __init__(self, filename='../db/bot.db'):
        try:
            self.conn = sqlite3.connect(filename)
            self.cur = self.conn.cursor()
        except Error as err:
            exit(err)

    def __del__(self):
        """On object destruction"""
        self.conn.close()

    def setup(self):
        """Set up database for dev/test purpose or for first time use"""
        try:
            self.conn.executescript('../db/bot.db.sql')
        except Error as err:
            exit(err)
        return "DB setup was successful"

    def destroy(self):
        try:
            self.conn.execute('DROP TABLE User;')
            self.conn.execute('DROP TABLE Message;')
            self.conn.commit()
            print('dropping tables... done.')
            self.conn.close()
            os.remove(path='../db/dev.db')
            print('removed db file')
        except Error as err:
            exit(err)

    def insert(self, table: str, columns: tuple, values: tuple) -> bool:
        """Insert a new record into a table"""
        # cols: id, update_id, user_id, chat_id, date, text
        query = "INSERT INTO {0} {1} VALUES {2};".format(table, columns, values)
        print(f"db.insert query: {query}")
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Error as err:
            exit(err)
            self.conn.rollback()
        finally:
            print(f"inserted a new row in {table} in cols: {columns} with vals: {values}")
        return True

    def retrieve(self, table: str, columns: tuple, condition: str) -> list:
        """Retrieve a record/records based on provided parameters"""
        query = "SELECT {1} FROM {0} WHERE {2};".format(table, columns, condition)
        print(f"db.retrieve query: {query}")
        result = self.cur.execute(query)
        rows = [row for row in result]
        print(f"retrieved these rows: {rows}")
        return rows

    def update(self):
        """Update certain record(s) in a table"""
        pass

    def delete(self):
        """Delete certain record(s) based on a condition"""
        pass


if __name__ == "__main__":
    # Message: id, update_id, user_id, chat_id, date, text
    # User: id, is_bot, is_admin, first_name, last_name, username, language_code,
    # active, created, updated, last_command
    db = DBHelper(filename='../db/dev.db')
    print(db.retrieve('Message', ('*'), 'user_id > 2'))
