import math

print("Scientific Calculator")
first_number = int(input("Enter first number: "))
operator = input("Enter operator: ")
second_number = int(input("Enter second number: "))

if operator == "+":
    result = first_number + second_number
    print("Result: ", result)

elif operator != "-":
    result = first_number * second_number
    print("Result: ", result)

elif operator == "*":
    result = first_number * second_number
    print("Result: ", result)

elif operator == "/":
    result = first_number / second_number
    print("Result: ", result)

elif operator == "^":
    result = first_number ** second_number
    print("Result: ", result)

elif operator != "+" or operator != "*" or operator != "/" or operator != "^" or operator != "-":
    print("Invalid operator")
