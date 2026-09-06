# import requests;
# response = requests.get("https://api.github.com")
# print(response.status_code)

print("hello")

temperature = 30
if temperature >= 30:
    print("It's hot")

txt_var = "25" # string
int_var = 25_25_22_525 # integer
float_var = 2.5 # float
bool_var = False # boolean

print(f"This is string {txt_var}")
print(f"This is integer {int_var}")
print(f"This is floating {float_var}")
print(f"This is boolean {bool_var}")

# type of them
print(type(txt_var))
print(type(int_var))
print(type(float_var))
print(type(bool_var))


print(11//3) # round and down

# Conditional statements

if True and False:
    print("or True")
else:
    print("or False")

# Repetition

str = '*' * 10
print(str)

# String methods

text = "Python Programming"

print(text.lower()) # "python programming"
print(text.upper()) # "PYTHON PROGRAMMING"
print(text.title()) # "Python Programming"

text = "$$ Python $ Progra$mming$$"
print(text.strip("$"))  # removes leading and trailing. -> "Python $ Progra$mming"

txt = "I love Python programming with Python"

# Check if something exists
print("Python" in txt) # True
print(txt.startswith("I")) # True
print(txt.endswith("Python")) # True

# Find position and frequency
print(txt.find("Python")) # 7 (first occurrence)
print(txt.count("Python")) # 2 (number of times)

# Replace
new_txt = txt.replace("Python", "JavaScript")
print(new_txt)  # "I love JavaScript programming with JavaScript"


# Loops

for i in range(5):
    print(f"{i} Hello!")

# Count from 1 to 5
for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

# Increment by 2
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8


# Loop through text

name = "Python".upper()
for letter in name:
    print(letter)


# Loop through a list

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")


# While loops
i = 0
while i<5:
    print(f"index: {i}")
    i+=1