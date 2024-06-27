myDictionary = {
    "name": "John",
    "age": 30,
    "isStudent": False
}

print(myDictionary)

# Dictionaries are unordered, meaning that the items have no defined order.
# Dictionaries are changeable, meaning that we can change the items after the dictionary has been created.

# Accessing Items
print(myDictionary["name"])
print(myDictionary.get("age"))

# Change Values
myDictionary["name"] = "Jane"
print(myDictionary)

# Get Keys
print(myDictionary.keys())

# Get Values
print(myDictionary.values())

# Get Items
print(myDictionary.items())

# Method	
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary