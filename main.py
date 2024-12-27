

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
       if amount > 0:
           self.balance += amount
           print(f"Deposited: {amount}$ to your account {self.owner} successfully.")
           return amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            print(f"insufficient account balance, withdraw cannot be preceded.")
        elif amount <= 0:
            print("Withdrawal cannot be negative")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn {amount}$ from your account {self.owner}")
            return amount

User1 = BankAccount("Dima", 3400)
User1.deposit(2600)
User1.withdraw(-200)

print(f"Your account balance: {User1.balance}$")