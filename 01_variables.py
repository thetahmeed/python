# creating a variable
name = "Tahmeed" # or name = 'Tahmeed'
age = 5
height = 5.9
doesSmoke = False

# print the variables
print(name)

# we can use the print() function to print multiple variables
print(name, age, height, doesSmoke)

# casting
age = str(age)
height = int(height)

# we can use thsese functions to convert data types
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean

# we can use the type() function to check the data type of a variable
print(type(age))

# we can use multiple variables in a single line
name, age, height = "Tahmeed", 5, 5.9

# unpacking a list
names = ["Tahmeed", "Tamim", "Tahsin"]
name1, name2, name3 = names # name1 = "Tahmeed", name2 = "Tamim", name3 = "Tahsin"

# we can use the same value for multiple variables
x = y = z = 1

# we can use the + operator to concatenate strings
print(name + " is " + str(age) + " years old")

# we can use the + operator to add numbers
print(5 + 5)

# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
