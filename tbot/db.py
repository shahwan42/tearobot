"""
    Database management module
"""
import sqlite3

from sqlite3 import Error


class DBHelper():

    def __init__(self, filename='../db/bot.db'):
        try:
            self.conn = sqlite3.connect(filename)
        except Error as err:
            exit(err)

    def create(self):
        """Create new record, and return it as Object of its type"""
        pass

    def retrieve(self):
        """Retrieve a record/records based on provided parameters"""
        pass

    def update(self):
        """Update certain record(s) based on a condition"""
        pass

    def delete(self):
        """Delete certain record(s) based on a condition"""
        pass
