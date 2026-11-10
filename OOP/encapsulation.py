class ATM:
    def __init__(self, init_amount):
        self.balance = init_amount

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Updated balance: {self.balance}"

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return f"Updated balance: {self.balance}"

    def view_balance(self):
        return f"Current balance: {self.balance}"


my_atm = ATM(2000)

print(my_atm.view_balance())
print(my_atm.deposit(500))
print(my_atm.withdraw(1000))
