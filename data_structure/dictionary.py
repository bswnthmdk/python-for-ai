# Creating dictionaries

my_dict = {} # Empty dictionary

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Different ways to create
scores = dict(math=95, english=87, science=92)
print(scores)

# Get values by key
print(person["name"]) # "Alice"
print(person["age"]) # 30

# Safer with get()
print(person.get("job")) # None (no error)
print(person.get("job", "Unknown")) # "Unknown" (default)

# Update multiple values
person.update({"age": 25, "job": "Engineer"})


# Changing dictionaries

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 60 # Update existing

# Remove items
del person["email"] # Remove by key
age = person.pop("age") # Remove and return
print(age) # 60
person.clear() # Remove all item

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])


# Nested dictionaries

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"]) # "A"
print(students["bob"]["age"]) # 21


# KeyError when key doesn't exist

person = {"name": "Alice"}

# Wrong
print(person["age"])  # KeyError!

# Right - use get()
print(person.get("age", 0)) # Returns 0 if missing


# Using mutable keys

# Wrong - lists can't be keys
bad_dict = {[1, 2]: "value"}  # TypeError!

# Right - use immutable types
good_dict = {(1, 2): "value"}  # Tuple is OK
good_dict = {"1,2": "value"}   # String is OK