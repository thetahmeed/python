'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
# Data Types
# Strings
a = "Hello World"	                        #str	
aa = 'Hello World'	                        #str
aaa = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt'''         #str

# Numeric
b = 20	                                    #int	
c = 20.5	                                #float	
d = 1j	                                    #complex	

# Sequence/Collection/List
e = ["apple", "banana", "cherry"]	        #list	
f = ("apple", "banana", "cherry")	        #tuple	(1)
g = range(6)	                            #range	(2)
h = {"name" : "John", "age" : 36}	        #dict	
i = {"apple", "banana", "cherry"}	        #set	(3)
j = frozenset({"apple", "banana", "cherry"})#frozenset	(4)

# Boolean
k = True	                                #bool	

# Binary
l = b"Hello"	                            #bytes	
m = bytearray(5)	                        #bytearray	
n = memoryview(bytes(5))	                #memoryview	

# None
o = None	                                #NoneType	

# setting the data type of a variable
p = str("Tahmeed")
q = int(5)
r = float(5.9)
s = bool(False)
# as well as complex(), list(), tuple(), range(), dict(), 
# set(), frozenset(), bytes(), bytearray(), memoryview(), NoneType()

# 1 The difference between list and tuple is that list is mutable, while tuple is immutable.
# Mutable means that the value can be changed after it is created.
# Immutable means that the value cannot be changed after it is created.

# 2 The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and stops before a specified number.

# 3 The difference between set and list is that set is unordered and unindexed,
# meaning that the items do not have a defined order, and cannot be accessed by index.

# 4 The difference between frozenset and set is that frozenset is immutable, while set is mutable.
# Immutable means that the value cannot be changed after it is created.


