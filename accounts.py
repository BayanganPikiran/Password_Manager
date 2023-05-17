import sqlite3
import random


class Account:

    def __init__(self, db_path):
        self.database = db_path
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.account_table = self.create_account_table()

    def create_account_table(self):
        account_table = self.cursor.execute("""CREATE TABLE accounts(
            website text,
            username text,
            password text)""")
        self.conn.commit()
        self.conn.close()
        return account_table

    def create_record(self, site, user, password):
        pass

    def update_record(self):
        pass

    def fetch_record(self):
        pass

    def delete_record(self):
        pass

    def generate_password(self):
        pass

    def retrieve_account(self):
        pass

    def delete_account(self):
        pass
