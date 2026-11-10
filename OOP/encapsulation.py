class ATM:
    def __init__(self, init_amount):
        self.__balance = init_amount

    def deposit(self, amount):
        self.__balance += amount
        return f"Updated balance: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return f"Updated balance: {self.__balance}"

    def view_balance(self):
        return f"Current balance: {self.__balance}"


my_atm = ATM(2000)

print(my_atm.view_balance())
print(my_atm.deposit(500))
print(my_atm.withdraw(1000))
