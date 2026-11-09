class Car:
    def __init__(self):
        self.type = ""
        self.fuel = "Petrol"

    def drive(self):
        return "The car is driving."


class Toyota(Car):
    def __init__(self):
        super().__init__()  # After calling the parent class constructor, the parent class attributes are initialized in the child object and can be accessed using self. The child class can also access inherited parent methods using self.
        self.name = "Toyota"
        self.type = "Mid-SUV"

    def show_details(self):
        return f"Name: {self.name}, Type: {self.type}, Fuel: {self.fuel}"


my_toyota = Toyota()

print(my_toyota.drive())  # Parent class function
print(my_toyota.show_details())  # Child class function
