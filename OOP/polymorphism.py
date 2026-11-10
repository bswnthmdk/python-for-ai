class Calculator_v1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


class Calculator_v2(Calculator_v1):
    def __init__(self, a, b, c):
        super().__init__(
            a, b
        )  # Calls the parent class constructor to initialize self.a and self.b
        self.c = c

    def addition(self):
        return super().addition() + self.c


calculator_v1 = Calculator_v1(10, 20)
print(calculator_v1.addition())

calculator_v2 = Calculator_v2(10, 20, 20)
print(calculator_v2.addition())


print(isinstance(calculator_v1, Calculator_v1))  # True

print(
    isinstance(calculator_v1, Calculator_v2)
)  # False; Calculator_v1 is not a subclass of Calculator_v2, so it is not an instance of Calculator_v2

print(
    isinstance(calculator_v2, Calculator_v1)
)  # True; Calculator_v2 is a subclass of Calculator_v1, so it is also an instance of Calculator_v1
