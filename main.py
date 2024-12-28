import sqlite3 as db

class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount: float ):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}$ to {self.owner}")
            self.update_db_data()
            return amount
        else:
            print("Deposit should be greater than zero")

    def withdraw(self,amount: float):
        if amount > self.balance:
            print(f"Insufficient account balance, you only have {self.balance}$ to withdraw")
        elif amount <= 0:
            print("Withdraw should be greater than zero")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn {amount}$, from your account")
            self.update_db_data()
            return amount

    def update_db_data(self):
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
    owner = str(input("Write your account name: ")).strip()

    with db.connect("bank.db") as con:
        cur = con.cursor()
        cur.execute("SELECT balance FROM users WHERE owner = ?", (owner,))
        data = cur.fetchone()

    if data:
        balance = data[0] # recieves current user balance from db, if user exists because data fetches in tuple using indexation to recieve data
        print(f"Hey {owner}! Glad to see you again, here's your account balance: {balance}$")

    else:
        first_deposit = float(input("Write your first deposit amount: "))

        if first_deposit <= 0:
            print("Deposit should be greater than 0.")

        print(f"Your account was created, your current balance is {first_deposit}$")

        with db.connect("bank.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (owner,balance) VALUES (?,?)", (owner,first_deposit))
            con.commit()

        balance = first_deposit

    account = BankAccount(owner, balance) #bankaccount object #usage as a self

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Show balance\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = float(input("Write your deposit amount: "))
            account.deposit(value)

        elif choice == 2:
            value = float(input("Write your withdrawal amount: "))
            account.withdraw(value)

        elif choice == 3:
            print(f"Here's your current balance: {account.balance}$, thanks {account.owner} for being with us !")

        elif choice == 4:
            print("See you later!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()