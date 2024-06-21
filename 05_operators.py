'''
    +	Addition	x + y	
    -	Subtraction	x - y	
    *	Multiplication	x * y	
    /	Division	x / y	
    %	Modulus	x % y	
    **	Exponentiation	x ** y	
    //	Floor division	x // y
'''

# Arithmetic Operators
x = 5
y = 3

# Addition
print(x + y) # 8

# Subtraction
print(x - y) # 2

# Multiplication
print(x * y) # 15

# Division
print(x / y) # 1.6666666666666667

# Modulus
print(x % y) # 2

# Exponentiation
print(x ** y) # 125 (5^3)

# Floor division
# The floor division // rounds the result down to the nearest whole number
print(x // y) # 1 (5/3 = 1.6666666666666667) 

# Assignment Operators
# =	    x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3
# := (walrus operator)	x := 5

# Comparison Operators
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y

# Logical Operators
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# Identity Operators
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y

# Membership Operators
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# Bitwise Operators
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

