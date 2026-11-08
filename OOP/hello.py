class Car:
    def __init__(self):
        self.company_name = ""
        self.model_name = ""

    def get_car(self):
        print(f"Car Company: {self.company_name} and Model: {self.model_name}")

    def set_car(self, company_name, model_name):
        self.company_name = company_name
        self.model_name = model_name


my_car = Car()
your_car = Car()


my_car.set_car("Toyota", "RAV4")
my_car.get_car()

your_car.set_car("Honda", "CRV")
your_car.get_car()
