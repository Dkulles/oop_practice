# to do 1.Add db for users data storage 2. Add transfers between accs 3(Maybe) Add loans
import sqlite3 as db


class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
       if amount > 0:
           self.balance += amount
           print(f"Deposited: {amount}$ to your account {self.owner} successfully.")
           self.update_balance_in_db()
           return amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            print(f"insufficient account balance, withdraw cannot be preceded.")
        elif amount <= 0:
            print("Withdrawal cannot be negative")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn {amount}$ from your account {self.owner}")
            self.update_balance_in_db()
            return amount

    def update_balance_in_db(self):
        with db.connect("bank.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE users SET balance = ? WHERE owner = ?", (self.balance, self.owner))
            con.commit()

def initialize_db():
     with db.connect("bank.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
        rowid INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT NOT NULL,
        balance REAL DEFAULT 0
        )""")
        con.commit()

def main():
    initialize_db()
