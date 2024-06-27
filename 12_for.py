avengers = ['ironman', 'thor', 'hulk', 'spiderman', 'captain america']

for avenger in avengers:
    print(avenger)

aString = 'My Name is Tahmeed'

for aChar in aString:
    print(aChar)

# Range
for x in range(6): # 0 to 5
    print(x)

for x in range(5, 10): # 5 to 9
    print(x)

for x in range(5, 10, 2): # 5 to 9, step 2
    print(x)

# Nested
abc = ['a', 'b', 'c']
xyz = ['x', 'y', 'z']

for a in abc:
    for x in xyz:
        print(a, x) 