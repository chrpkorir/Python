# Ask the user to input 2 numbers
num1, num2 = input('Enter 2 numbers: ').split()

# Convert the strings into regular Integers
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 - num2

# Multiply the values and store in product
product = num1 * num2

#Divide the numbers and store in quotient
quotient = num1 / num2

#Use modulus on the values to find the remainder
remainder = num1 % num2

#print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
