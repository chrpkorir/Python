# Program start 

# Miles to kilometer converter func
# In mind 1 mile == 1.61 km

import os
import getpass

# Miles to kilometers
def mile_to_km(mile):
    res = float(mile) * 1.61
    print(mile, 'miles =', round(res, 2), 'kilometers')


# Ksh to US Dollars
# In mind 1ksh = 109.80 USD
def ksh_to_usd(ksh):
    res = float(ksh) * 109.80
    print(ksh, 'Kenyan shilings =', round(res, 2), 'US Dollars')

# Percent to letter grade
def percent_to_letter_grade(percent):
    p = int(percent)
    if p >= 80 and p <= 100:
        print(str(p) + '%', '=', 'A')
    # if percent in range(80, 100):
    #     print(str(percent) + '%', '=', 'A')
    elif p >= 70 and p < 80:
        print(str(p) + '%', '=', 'B')

    elif p >= 60 and p < 70:
        print(str(p) + '%', '=', 'C')

    elif p >= 50 and p < 60:
        print(str(p) + '%', '=', 'D')

    elif p >= 20 and p < 40:
        print(str(p) + '%', '=', 'E')

    elif p >= 0 and p < 20:
        print(str(p) + '%', '=', 'F')

# Kilograms into pounds(lbs)
# 1 kg == 2.20 lbs
def kg_to_lbs(kg):
    res = float(kg) * 2.20
    print(kg, 'kilograms is', round(kg, 2),'Pounds(lbs)')

# Centimeter into inches
# 1cm == 0.393701 inches
def cm_to_inches(centimeter):
    inches = 0.393701
    res = float(centimeter) * inches
    print(centimeter + ' centimeters is', res, 'Inches')





name = input('Please enter your name: ').capitalize()

print('Hello',name+',','Welcome to your personal unit converter.')

# choice = input('Please choose which conversion you would like to perform:\n'
# '1 - Convert miles into kilometers\n'
# '2 - Convert Kenyan shilings into US Dollars\n'
# '3 - Convert percent to letter grade\n'
# '4 - Convert kilograms into pounds(lbs\n'
# '5 - Convert centimeters into inches\n'
# )

print('Please choose which conversion you would like to perform:\n'
'1 - Convert miles into kilometers\n'
'2 - Convert Kenyan shilings into US Dollars\n'
'3 - Convert percent to letter grade\n'
'4 - Convert kilograms into pounds(lbs\n'
'5 - Convert centimeters into inches\n')


choice = input('Choice: ')

if choice == str(1):
    mile = input("Value in miles to convert in km: ")
    mile_to_km(mile)

elif choice == str(2):
    ksh = input("Value in Kenyan shilings to convert in US Dollars: ")
    ksh_to_usd(ksh)

elif choice == str(3):
    percent = input('Percent to convert to letter grade: ')
    percent_to_letter_grade(percent)

elif choice == str(4):
    kilograms = input('Value in Kilograms to convert into pounds(lbs): ')
    kg_to_lbs(kilograms)

elif choice == str(5):
    cm = input('Value in centimeters to convert into inches: ')
    cm_to_inches(cm)

print('Goodbye', name)


"""
program start 

define function to convert mile to kilometer
Begin Function
function mile_to_km (mile)
    Set Result TO mile * 1.61
    print Result
End Function

Begin Function
function ksh_to_usd (ksh)
    Set Result TO float(ksh) * 109.80
    print Result
End Function

Begin Function
function cm_to_inches(centimeter)
    Set Inches TO 0.393701
    Set Result TO float(centimeter) * inches
    print Result
End Function

Begin Function
function kg_to_lbs(kg)
    Set Result TO float(kg) * 2.20
    print Result
End Function

Begin Function
function percent_to_letter_grade(percent)
    Set percent variable
    if percent >= 80 and percent <= 100:
        print 'A'

    elif percent >= 70 and percent < 80:
        print 'B'

    elif percent >= 60 and percent < 70:
        print 'C'

    elif percent >= 50 and percent < 60:
        print 'D'

    elif percent >= 20 and percent < 40:
        print 'E'

    elif percent >= 0 and percent < 20:
        print 'F'

End Function


set name = prompt user for input
print greetings name

print('Please choose which conversion you would like to perform:\n'
'1 - Convert miles into kilometers\n'
'2 - Convert Kenyan shilings into US Dollars\n'
'3 - Convert percent to letter grade\n'
'4 - Convert kilograms into pounds(lbs\n'
'5 - Convert centimeters into inches\n')

set choice = prompt user for a number input

if choice == one:
    set mile = prompt user for a value to convert
    function call mile_to_km (mile)

elif choice == two:
    set ksh = prompt user for a value to convert
    function call ksh_to_usd (ksh)

elif choice == three:
    set percent = prompt user for Value
    function call percent_to_letter_grade(percent)

elif choice == four:
    set kg = prompt user for value
    function call kg_to_lbs(kg)

elif choice == five:
    set centimeter = prompt user for Value
    function call cm_to_inches(centimeter)

print Goodbye name
pseudocode for converter program
"""