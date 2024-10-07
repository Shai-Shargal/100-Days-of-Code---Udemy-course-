def add(n1, n2):
    return n1 + n2

def sub(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2


operations = { "+" : add , "-" : sub , "*": multiply , "/": divide }

def get_number(prompt):
    """Get valid number input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """Get valid operation symbol from the user."""
    while True:
        operation_symbol = input("Pick an operation (+, -, *, /): ")
        if operation_symbol in operations:
            return operation_symbol
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

def calculator():
    """Main calculator function with loop for multiple calculations."""
    while True:

        number1 = get_number("Enter first number: ")
        operation_symbol = get_operation()
        number2 = get_number("Enter second number: ")


        calculation_function = operations[operation_symbol]
        result = calculation_function(number1, number2)


        print(f"{number1} {operation_symbol} {number2} = {result}")


        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break


calculator()
