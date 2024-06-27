# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200

if a == b:
    print("a is equal to b")
elif a< b:
    print("a is less than b")
else: 
    print("a is greater than b")

# Short Hand/Ternary Operator
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

# And
c = 40
if a > b and c > a:
    print("Both conditions are True")

# Or
if a > b or c > a:
    print("At least one of the conditions is True")

# Not
if not a > b:
    print("a is not greater than b")

# Nested If
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else :
    print("Not above ten.")

# Pass Statement
a = 11
b = 23

if b > a:
    pass