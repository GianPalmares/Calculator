
# Function to perform addition
def addition(num1, num2):
    return print(f"{round(num1 + num2, 2)}")

# Function to perform subtraction
def subtraction(num1, num2):
    
    # Check if num1 is less than num2
    if num1 < num2:
        
        # Ask user if they want to continue with the subtraction or swap the inputs
        choice = input("This will return a minus answer, do you want to continue or swap the inputs around?(y/n): ").lower()
        
        # If user chooses to continue, perform subtraction with original order
        if choice == "y":
            return print(f"{round(num1 - num2, 2)}")
        
        # If user chooses to swap, perform subtraction with swapped order
        elif choice == "n":
            return print(f"{round(num2 - num1, 2)}")
        
        # If user provides an invalid input, prompt them to choose between 'y' and 'n'
        else:
            return print("Need to choose between(y/n)")
    
    # If num1 is not less than num2, perform subtraction with original order
    return print(f"{round(num1 - num2, 2)}")

# Function to perform multiplication
def multiplication(num1, num2):
    return print(f"{round(num1 * num2, 2)}")

# Function to perform division
def division(num1, num2):
    
    # Check if num2 is 0, which would result in division by zero
    if num2 == 0:
        
        # Ask user if they want to continue and break the program or swap the inputs
        choice = input("This will return infinity, do you want to continue and break the program or swap the inputs around?(y/n): ").lower()

        # If user chooses to continue, print a message and perform division with original order
        if choice == "y":
            print("\nYou are a psychopath!!!")
            return print(f"{round(num1 / num2, 2)}")
        
        # If user chooses to swap, perform division with swapped order
        elif choice == "n":
            return print(f"{round(num2 / num1, 2)}")
        
        # If user provides an invalid input, prompt them to choose between 'y' and 'n'
        else:
            return print("Need to choose between(y/n)")

    # If num2 is not 0, perform division with original order
    return print(f"{round(num1 / num2, 2)}")

# Function to perform modulus
def modulus(num1, num2):
    
    # Check if num2 is 0, which would result in modulus by zero
    if num2 == 0:
        
        # Ask user if they want to continue and break the program or swap the inputs
        choice = input("This will return infinity, do you want to continue and break the program or swap the inputs around?(y/n): ").lower()

        # If user chooses to continue, print a message and perform modulus with original order
        if choice == "y":
            print("\nYou are a psychopath!!!")
            return print(f"{round(num1 % num2, 2)}")
        
        # If user chooses to swap, perform modulus with swapped order
        elif choice == "n":
            return print(f"{round(num2 % num1, 2)}")
        
        # If user provides an invalid input, prompt them to choose between 'y' and 'n'
        else:
            return print("Need to choose between(y/n)")

    # If num2 is not 0, perform modulus with original order
    return print(f"{round(num1 % num2, 2)}")

# Function to perform exponentiation
def power(num1, num2):
    return print(f"{round(num1 ** num2, 2)}")


# Infinite loop to keep asking for user input until a valid operation is performed or valid input is received
while True:
    try:

        # Get user input for two numbers and the operator
        num1 = float(input("\nPlease enter the first number: "))
        num2 = float(input("Please enter the second number: "))

        operator = input("\nPlease enter operator (+, -, *, /, %, **): ")

        # Perform the corresponding operation based on the operator entered
        if operator == "+":
            addition(num1, num2)
            
        elif operator == "-":
            subtraction(num1, num2)
            
        elif operator == "*":
            multiplication(num1, num2)
            
        elif operator == "/":
            division(num1, num2)
            
        elif operator == "%":
            modulus(num1, num2)
            
        elif operator == "**":
            power(num1, num2)
            
        else:
            # If an invalid operator is entered, prompt the user to enter a valid one
            print("\nPlease enter a valid operator (+, -, *, /, %, **)!")
            continue
        
        # Break out of the loop if a valid operation is performed
        break

    except Exception:
        # If the user enters non-numeric input for numbers, catch the ValueError and ask for input again
        print("\nInvalid input. Please enter numeric values for numbers.")

