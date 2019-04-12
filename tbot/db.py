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
        """Create new record"""
        pass

    def retrieve(self):
        """Retrieve a record based on provided parameters"""
        pass

    def update(self):
        """Update a certain record based on a condition"""
        pass

    def delete(self):
        """Delete a certain record based on a condition"""
        pass
