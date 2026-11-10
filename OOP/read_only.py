class Bank:
    def __init__(self, init_amount):
        self.__acc_no = 1234567890
        self._balance = init_amount

    # @property allows this method to be accessed like an attribute
    # It makes get_account_number read-only because no setter is defined
    @property
    def get_account_number(self):
        return self.__acc_no


my_bank = Bank(5000)

# Accessing the property without parentheses
# print(my_bank.get_account_number()) # Error: () shoudn't be used when accessing a property.
print(my_bank.get_account_number)

# This will raise an error because get_account_number is read-only
# my_bank.get_account_number = 9876543210
