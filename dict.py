"""
used to store key-value pairs

"""

my_dict = {} # empty dictionary
print(my_dict)

my_dict={1:'python',2:'ruby'} # dictionary wwith elements
print(my_dict)


# Changing and adding key, value pairs

my_dict[2]= ' Java' # changing element
print(my_dict)

my_dict[3] = 'Javascript' # adding key value pair
print(my_dict)

# Deleting key value pairs

my_dict = {1:'python', 2:'java', 3:'ruby'}
a = my_dict.pop(3) # deleting element
print("value",a)
print(my_dict)

b = my_dict.popitem() # deleting key value pair
print('key,value,pair',b)
print('Dictionary',my_dict)

my_dict.clear()
print('n',my_dict)
