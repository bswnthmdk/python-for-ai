# Creating Tuple
my_tuple = ()

point = (3, 5)
colors = ("red", "green", "blue", "yellow", "white")

single = (42,)  # Note : Single item tuple needs comma!
not_tuple = (42) # Without the comma, Python thinks it’s just parentheses around a number!

print(point)
print(colors)
print(colors[-2])
print(colors[2:4])

# Tuple unpacking
point = (3, 5)
x, y = point  # x = 3, y = 5
print(x)

# Common mistakes

# Forgetting comma in single tuple
# Wrong - not a tuple
single = (42)
print(type(single))  # <class 'int'>

# Right - include comma
single = (42,)
print(type(single))  # <class 'tuple'>

# Trying to modify tuples
# Wrong - tuples are immutable
point = (3, 5)
# point[0] = 4  # TypeError!

# Right - create a new tuple
point = (4, point[1])
# Or convert to list, modify, convert back
temp = list(point)
temp[0] = 2
point = tuple(temp)
print(point)

