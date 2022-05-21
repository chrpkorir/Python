""" Data structures allows you to organize you data in 
such a way that that enables you to store collection of data , 
relate them and perfor operations onthem accordingly
"""

# List store data of different data type in a sequential manner.

# creating a list

my_list =[] # crrates an empty list
print(my_list)

my_list=[1,3,4,'examples',3.124] # craetes list with data
print(my_list)

"""
Adding elements in a list
append()- adds all the elements passed as a single element
extend()- adds the elements one-by-one
insert()- adds elements passed to the index function 
          and increase the size of the list too

"""

my_list=[1,2,3]
print(my_list)

my_list.append([555,12]) # adds as a single element
print(my_list)

my_list.extend([234,'more_examples']) # Add as different elements
print(my_list)

my_list.insert(1,'insert_examles') # add element i 
print(my_list)

"""
To delete elements use del keyword
To have them back use use the pop() function which takes the index value
To remove an element by its value use the remove() function 
"""


my_list=[1,3,4,'examples',3.124,10,30] 
del my_list[5] # deletes the element at index 5
print(my_list)

my_list.remove('examples') # removes element with value
print(my_list)

a = my_list.pop(1) #pop element from list
print('Popped element:',a,'list remaining:',my_list)


my_list.clear()# empty the list
print(my_list)


# Accessing elements/ Strings in python


my_list=[1,3,4,'examples',3.124,10,30] 
for element in my_list: # access elements one by one
    print(element)

    print(my_list) # access all the elements

    print(my_list[3]) #  access index 3 element

    print(my_list[0:2]) # access tyhe element from 0 to 1 and excludes 2

    print(my_list[:-1]) # access elements in reverse


"""
len()- returns to us the length of the list
index()- finds the index function value of values passed 
      when it has been encountered the 1st time
count()- finds the count of the values passed to it
sorted()/sort()- sort the   values of the list    
"""    

my_list=[1,10,30,10]
print(len(my_list)) # find the length of the list

print(my_list.indes(10)) # find the index of element that occurs first

print(my_list.count(10)) # find countof the elements

print(sorted(my_list)) # print sorted list but not change the original 

my_list.sort(revers=True) # sort original list
print(my_list)




