x = 0

while x < 10 :
    print(x)
    x=x+1

# Break and Continue
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1

while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)

# Else in While Loop
while x < 10:
    print(x)
    x += 1
else:
    print("x is no longer less than 10")