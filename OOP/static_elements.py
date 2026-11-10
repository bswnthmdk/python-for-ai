class Student:
    name = "John Doe"  # Static/Class attribute

    def __init__(self, age):
        self.age = age

    # decorators
    @staticmethod
    def display_name():
        return f"Name: {Student.name}"

    def display_age(self):
        return f"Age: {self.age}"


# Accesssing static/class attribute and method without creating an instance of the class
print(Student.name)
print(Student.display_name())

# Accesssing non-static attribute and method
student1 = Student(20)
print(student1.display_age())
