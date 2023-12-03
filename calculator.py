
# Function to perform addition
def addition(num1, num2):
    return print(f"\nThe sum of {num1} {operator} {num2} is {round(num1 + num2, 2)}\n")


# Function to perform subtraction
def subtraction(num1, num2):

    # Check if num1 is less than num2
    if num1 < num2:
        
        # Error handling for choice input
        while True:

            # Ask user if they want to continue with the subtraction or swap the inputs
            choice = input("\nThis will return a minus/negative answer, do you want to continue or swap the inputs around?(y/n): ").lower().strip()

            # If user chooses to continue, perform subtraction with original order
            if choice == "y":
                break

            # If user chooses to swap, perform subtraction with swapped order
            elif choice == "n":
                return print(f"\nThe difference between {num2} {operator} {num1} is {round(num2 - num1, 2)}\n")
            
            # If user provides an invalid input, prompt them to choose between 'y' and 'n'
            else:
                print("Need to choose between(y/n)")
                continue
    
    # If num1 is not less than num2, perform subtraction with original order
    return print(f"\nThe difference between {num1} {operator} {num2} is {round(num1 - num2, 2)}\n")


# Function to perform multiplication
def multiplication(num1, num2):
    return print(f"The product between {num1} {operator} {num2} is {round(num1 * num2, 2)}\n")


# Function to perform division
def division(num1, num2):
    
    # Check if num2 is 0, which would result in division by zero
    if num2 == 0:
        
        # Error handling for choice input
        while True:

            # Ask user if they want to continue and break the program or swap the inputs
            choice = input("\nThis will return infinity, do you want to continue and break the program or swap the inputs around?(y/n): ").lower().strip()

            # If user chooses to continue, print a message and perform division with original order
            if choice == "y":
                print("You are a psychopath!!! Let me ask you again...")
                # If the comment(#) below gets removed it will break the code
                # return print(f"{round(num1 / num2, 2)}")
                continue

            # If user chooses to swap, perform division with swapped order
            elif choice == "n":
                return print(f"\nThe quotient between {num2} {operator} {num1} is {round(num2 / num1, 2)}\n")
            
            # If user provides an invalid input, prompt them to choose between 'y' and 'n'
            else:
                print("Need to choose between(y/n)")
                continue

    # If num2 is not 0, perform division with original order
    return print(f"\nThe quotient between {num1} {operator} {num2} is {round(num1 / num2, 2)}\n")


# Function to perform modulus
def modulus(num1, num2):
    
    # Check if num2 is 0, which would result in modulus by zero
    if num2 == 0:
        
        # Error handling for choice input
        while True:

            # Ask user if they want to continue and break the program or swap the inputs
            choice = input("\nThis will return infinity, do you want to continue and break the program or swap the inputs around?(y/n): ").lower().strip()

            # If user chooses to continue, print a message and perform modulus with original order
            if choice == "y":
                print("You are a psychopath!!! Let me ask you again...")
                # If this comment gets removed it will break the code
                # return print(f"{round(num1 % num2, 2)}")
                continue
            
            # If user chooses to swap, perform modulus with swapped order
            elif choice == "n":
                return print(f"\nThe remainder between {num2} {operator} {num1} is {round(num2 % num1, 2)}\n")
            
            # If user provides an invalid input, prompt them to choose between 'y' and 'n'
            else:
                print("Need to choose between(y/n)")
                continue

    # If num2 is not 0, perform modulus with original order
    return print(f"\nThe remainder between {num1} {operator} {num2} is {round(num1 % num2, 2)}\n")


# Function to perform exponentiation
def power(num1, num2):
    return print(f"\nThe result between {num1} raised to the power(**) of {num2} is {round(num1 ** num2, 2)}\n")


# Infinite loop to keep asking for user input until a valid operation is performed or valid input is received
# Error handling for num1
while True:
    try:

        # Get user input for num1
        num1 = float(input("\nPlease enter the first number: "))
        break

    except Exception:
        # If the user enters non-numeric input for numbers, catch the ValueError and ask for input again
        print("Invalid input! Please enter a numeric value.")


# Infinite loop to keep asking for user input until a valid operation is performed or valid input is received
# Error handling for num2
while True:
    try:

        # Get user input for num2
        num2 = float(input("\nPlease enter the second number: "))
        break

    except Exception:
        # If the user enters non-numeric input for numbers, catch the ValueError and ask for input again
        print("Invalid input! Please enter a numeric value.")


# Error handling for operator
while True:
    
    operator = input("\nPlease enter operator (+, -, *, /, %, **): ").strip()

    # Perform the corresponding operation based on the operator entered
    if operator == "+":
        addition(num1, num2)
        break
        
    elif operator == "-":
        subtraction(num1, num2)
        break

    elif operator == "*":
        multiplication(num1, num2)
        break
        
    elif operator == "/":
        division(num1, num2)
        break

    elif operator == "%":
        modulus(num1, num2)
        break

    elif operator == "**":
        power(num1, num2)
        break

    else:
        # If an invalid operator is entered, prompt the user to enter a valid one
        print("Invalid operator! Please enter a valid operator from these choices (+, -, *, /, %, **)!")
        continue
