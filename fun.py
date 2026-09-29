def greet():
    print("Good Morning!")
greet()

count = 10
def increament():
    global count
    count += 1
    print(count)
increament()

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8