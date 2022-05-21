import os

# main mennu function
def main_menu():
    os.system("clear")
    print("SIMPLE CALCULATOR PROGRAM")
    print("\nOPTIONS")
    print("[1]-ADDITION")
    print("[2]-SUBTRACTION")
    print("[3]-MULTIPLICATION")
    print("[4]-DIVITION")
    print("[0]-EXIT PROGRAM")

# user input
option = input("\nEnter option: ")

# enter the correct option
while option not in ["1", "2", "3", "4", "0"]:
    print("Invalid Option!")
    # option = input("\nEnter Option: ")

    # call the function that matchs the option
    if option == "1":
        Add()
    elif option == "2":
        subtract()
    elif option == "3":
        multiply()
    elif option == "4":
        divide()
    elif option == "0":
        exit_program()

# add function
def add():
    os.system("clear")
    print("[1]-ADDITION")
    num1 = int(input("\nEnter First Number:"))
    num2 = int(input("\nEnter Second Number:"))
    ans_1 = num1 + num2
    print("The answer is ", float(ans_1))
    os.system("pause")

    # back to the main menu
    main_menu()

# subtract function
def subtract():
    os.system("clear")
    print("[2] - SUBTRACTION")
    num1 = int(input("\nEnter First Number: "))
    num2 = int(input("Enter Second Number: "))
    ans_1 = num1 - num2
    print("the answer is ", float(ans_1))
    os.system("pause")

    #  back to the main program
    main_menu()

# multiply function
def multiply():
    os.system("clear")
    print("[3] - MULTIPLICATION")
    number1 = int(input("\nEnter First Number: "))
    number2 = int(input("Enter Second Number: "))
    ans_1 = number1 * number2
    print("the answer is ", float(ans_1))
    os.system("pause")

    # back to the main program
    main_menu()

# divide function
def divide():
    os.system("clear")
    print("[4] - DIVISION")
    num1 = int(input("\nEnter First Number: "))
    num2 = int(input("Enter Second Number: "))

    # holds the operation when the user performs division
    if (num2 == 0):
        print("Error! Division by Zero!")
        divide()
    else:
        ans_1 = num1 / num2
        print("the answer is ", float(ans_1))
        os.system("pause")

    # back to the main program
    main_menu()


# exit function
def exit_program():
    os.system("clear")


# ask the user to exit/stay in the application
print("[0]-EXIT PROGRAM")
exit = input("\nExit Calculator?(y/n)")

# loop
while exit not in ["y", "n"]:
    print("Invalid Input!")
    exit = input("\nExit calculator?(Y/N) ")

# after the loop
if exit == "y":
    print("Thank you")
    exit()
elif exit == "n":
    # back to main menu
    main_menu()

#calling the main ptogram
main_menu()