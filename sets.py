"""
Sets are collection of unordered elements that are unique
"""

my_set = { 1,2,3,3,4,5,5,5}
print(my_set)

# Adding elements

my_set = {1, 2, 3}
my_set.add(4) #add element to set
print(my_set)


# operation in a set

my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set | my_set_2) # union() combines the data present in both sets.
print(my_set.intersection(my_set_2), '--------', my_set & my_set_2)# intersection() finds the data present in both sets only.
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)# difference() function deletes the data present in both and outputs data
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)
#  symmetric_difference() does the same as the difference() function but outputs 
# the data which is remaining in both sets.