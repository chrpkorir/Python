"""
Tuples are same as list with  the exception that the 
data cannot be changes once entered no matter what
"""

my_tuple = (1,2,3) # creatin a tuple
print(my_tuple)

my_tuple2 = (1,2,3,'faith') # accessing the tuple
for i in my_tuple2:
    print(i)
print(my_tuple)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple2[3][4])

# Append elements

my_tuple = (1, 2, 5)
my_tuple = my_tuple + (4, 5, 6) #add elements
print(my_tuple)
