import sqlite3


class Account:

    def __init__(self, db_path):
        self.database = db_path
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.account_table = self.create_accounts_table()

    def create_accounts_table(self):
        accounts_table = self.cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
            id integer PRIMARY KEY AUTOINCREMENT, 
            website text NOT NULL,
            username text NOT NULL,
            password text,
            UNIQUE(website, username))""")
        self.conn.commit()
        return accounts_table

    def create_record(self, website, username, password):
        try:
            self.cursor.execute("INSERT OR ABORT INTO accounts (website, username, password) VALUES (?, ?, ?)",
                                (website, username, password))
        except sqlite3.IntegrityError:
            pass
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

    def delete_record(self, site, username):
        delete = "DELETE from accounts WHERE website=? AND username=?"
        parameters = (site, username)
        self.cursor.execute(delete, parameters)
        self.conn.commit()

    def generate_password(self):
        pass

    def retrieve_account(self):
        pass

    def delete_account(self):
        pass
