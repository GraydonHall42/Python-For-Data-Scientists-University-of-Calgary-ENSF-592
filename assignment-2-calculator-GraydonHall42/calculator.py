# calculator.py
# AUTHOR NAME: Graydon Hall
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 2 git repository.
#


def calculator_main():
    """
    main calculator function, where equation is obtained from user, solved, and then result is printed to terminal.
    """
    user_equation = obtain_user_equation()  # function called to obtain equation from user as a string

    # note: pythons eval() function *****Automatically uses correct order of operations***
    result = eval(user_equation)  # calculated result based on pythons eval() function

    print(f"Your result: {user_equation} = {result}")  # equation and solution to user


def obtain_user_equation():
    """
    function used to obtain input from user for values and operations they want to perform
    User will provide 3 integers and 2 operations
    :return: string representation of the equation user wants to solve
    """
    int1 = obtain_user_int("Enter the first value as an integer: ")
    op1 = obtain_user_operator("Enter the first operator: ")
    int2 = obtain_user_int("Enter the second value as an integer: ")
    op2 = obtain_user_operator("Enter the second operator: ")
    int3 = obtain_user_int("Enter the third value as an integer: ")
    string_formula = f"{int1}{op1}{int2}{op2}{int3}"  # string representation of the user input.
    return string_formula


def obtain_user_int(message):
    """
    Obtain integer value from user.
    Added error handling for non integer values as bonus points.
    :param message: message to be displayed to user
    :return: integer value supplied by user
    """

    while True:  # loop runs till user enters valid integer entry.
        try:  # ask for user input. attempt to cast to integer and return value
            return int(input(f"{message} "))
        except:
            # exception will occur if provided input is not an integer
            print("Invalid input: Please Provide an Integer")  # message informing user of error


def obtain_user_operator(message):
    """
    function used to obtain calculator operator from the user
    :param message: message to be displayed to the user
    :return: returns a parameter which is specified by the user
    """
    valid_operators = ['+', '-', '/', '*']  # define legal operators
    while True:  # loop operates till valid user input is supplied
        user_operator = input(message)
        if user_operator in valid_operators:  # check if operator is one of our legal operators
            return user_operator
        else:
            print("Invalid input, please enter one of the following: + - / =")


calculator_main()  # call our main function in initiate the program

# SOURCES:

# Convert string input to int or float to check if it is a number
# https://pynative.com/python-check-user-input-is-number-or-string/#:~:text=To%20check%20if%20the%20input%20string%20is%20an%20integer%20number,using%20the%20int()%20constructor.&text=To%20check%20if%20the%20input%20is%20a%20float%20number%2C%20convert,using%20the%20float()%20constructor.

# eval() function
# https://realpython.com/python-eval-function/
