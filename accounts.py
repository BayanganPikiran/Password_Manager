import sqlite3
import random


class Account:

    def __init__(self, db_path):
        self.database = db_path
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.account_table = self.records_accounts_table()

    def record_already_exists(self, site, user):
        is_record_query = "SELECT * FROM accounts WHERE EXISTS website=? AND username=?"
        parameters = (site, user)
        self.cursor.execute(is_record_query, parameters)
        self.conn.commit()

    def records_accounts_table(self):
        records_table = self.cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
            record_id INTEGER PRIMARY KEY, 
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL)""")
        self.conn.commit()
        return records_table

    def create_record(self, site, user, password):
        create_record = "INSERT INTO accounts (website, username, password) VALUES (?, ?, ?)"
        parameters = (site, user, password)
        self.cursor.execute(create_record, parameters)
        self.conn.commit()

    def confirm_record_input(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor.execute("SELECT * FROM accounts")
        print(self.cursor.fetchall())
        self.conn.commit()

    def update_record(self, password, site, user):
        update = "UPDATE accounts SET password=? WHERE website=? AND username=?"
        parameters = (password, site, user)
        self.cursor.execute(update, parameters)
        self.conn.commit()

    def fetch_password(self, site, user):
        query = "SELECT password FROM accounts WHERE website=? AND username=?"
        parameters = (site, user)
        self.cursor.execute(query, parameters)
        items = self.cursor.fetchall()
        for item in items:
            password = str(item).strip("'()',")
            return password

    def delete_record(self, site, user):
        delete = "DELETE from accounts WHERE website=? AND username=?"
        parameters = (site, user)
        self.cursor.execute(delete, parameters)
        self.conn.commit()
