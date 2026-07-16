# Creating List
my_list = [] # Empty list

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # Last index excluded, -> ["apple", "banana"]
print(fruits[1:])  # ["banana", "orange"]

# Add items
fruits.append("grape") # Add to end
fruits.insert(1, "kiwi") # Insert at position & shift others to the right

# Remove items
fruits.remove("banana") # Remove by value
last = fruits.pop() # Remove and return last
print(last)

del fruits[0] # Remove by index

print(fruits)


# List methods

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers)) # 6 (length)
print(numbers.count(1)) # 2 (count occurrences)
print(numbers.index(4)) # 2 (find position)

# Sorting
numbers.sort() # Sort in place
print(numbers) # [1, 1, 3, 4, 5, 9]

numbers.reverse() # Reverse order
print(numbers) # [9, 5, 4, 3, 1, 1]

numbers.copy() # Create and return a copy

# Checking lists

fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")


# Shallow copy issues

# Wrong - both variables point to same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - changed!

# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged