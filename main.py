import math


def scientific_calculator():
    global second_number
    print("Scientific Calculator")

    # Using float to allow for decimals
    try:
        first_number = float(input("Enter first number: "))
    except ValueError:
        print("Invalid input for the first number.")
        return

    operator = input("Enter operator (+, -, *, /, ^): ").strip()

    # For binary operations, require a second number
    if operator in {"+", "-", "*", "/", "^"}:
        try:
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input for the second number.")
            return

    # Calculation based on operator
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = first_number / second_number
    elif operator == "^":
        result = first_number ** second_number
    else:
        print("Invalid operator. Please use one of: +, -, *, /, ^")
        return

    print("Result:", result)


if __name__ == "__main__":
    scientific_calculator()
