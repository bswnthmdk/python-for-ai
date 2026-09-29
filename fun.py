def greet():
    print("Good Morning!")
greet()

count = 10
def increament():
    global count
    count += 1
    print(count)
increament()

def add_numbers(a, b=0):
    return a + b

print(add_numbers(5, 3))  # 8: both parameters supplied
print(add_numbers(5))     # 5: uses the default value for b

# Wrong - don't use lists as defaults
def add_item(item, list=[]):
    list.append(item)
    return list

# Right - use None and create new list
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list

print(add_item("apple"))  # ['apple']