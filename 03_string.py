s = 'Tahmeedul Islam'

# Length of the string
print(len(s))

# Accessing characters in a string
print(s[0]) # T

# Slicing
print(s[0:7]) # Tahmeed

# Negative Indexing
print(s[-5:-1]) # Isla

# String Methods
print(s.upper()) # TAHMEEDUL ISLAM

print(s.lower()) # tahmeedul islam

print(s.strip()) # Tahmeedul Islam (removes any whitespace from the beginning or the end)

print(s.replace("Tahmeedul", "Tahmeed")) # Tahmeed Islam

print(s.split(" ")) # ['Tahmeedul', 'Islam']

# Check String
print("Tahmeed" in s) # True

print("Tahmeed" not in s) # False

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b

print(c) # Hello World

# String Format
age = 5
txt = "My name is Tahmeed, and I am {}"
print(txt.format(age)) # My name is Tahmeed, and I am 5

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # We are the so-called "Vikings" from the north.

# loop through a string
for x in "banana":
  print(x)

# String Methods
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found