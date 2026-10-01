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
# Reason - The default list is created once when the function is defined, so it’s reused across calls
def add_item(item, items=[]):
    items.append(item)
    return items

# The second call includes the first item because the default list is reused:
print(add_item("apple"))  # ['apple']
print(add_item("banana"))  # ['apple', 'banana']

# Right - use None and create new list
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("apple"))  # ['apple']
print(add_item("banana"))  # ['banana']



# Returning multiple values

def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)
