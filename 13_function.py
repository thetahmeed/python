def sum(a, b):
    return a+b

print(sum(1,1))
print(sum(a=2,b=2))

# Arbitrary Arguments, *args
# If we are not sure about how many the arguments could be
# This way the function will receive a tuple of arguments, and can access the items accordingly
def printNames(*names):
    print(names[0])
    print(names[1])
    print(names[2])

printNames('Tahmeed', 'Tamim', 'Tasin')

# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name
def printNames(**x):
    print(x['a'])
    print(x['b'])

printNames(a='dfd', b='sfd')

# Default Parameter Value
def printName(name='Tahmeed'):
    print(name)

printName('Tamim')
printName()

# Positional-Only Arguments
# If you want to make sure that the function is called with positional arguments only
# place a / before the parameter name
# Positional-only: The parameters must be passed by position. Ex: printName('Tahmeed')
def printName(name, /):
    print(name)

printName('Tahmeed')

# Keyword-Only Arguments
# If you want to make sure that the function is called with keyword arguments only
# place a * before the parameter name
# Keyword-only: The parameters must be passed by keyword. Ex: printName(name='Tahmeed')
def printName(*, name):
    print(name)

printName(name='Tahmeed')