#!/usr/bin/python3

def calculate(operator, x, y):
    if operator == "*" or operator == "multiply":
        return x * y
    if operator == "/" or operator == "divide":
        return x / y
    if operator == "+" or operator == "add":
        return x + y
    if operator == "-" or operator == "subtract":
        return x - y

def main():
    while True:
        try:
            x = float(input("Enter a number: "))
            y = float(input("Enter another number: "))
            break
        except:
            print("Invalid input. Try again.")

    operator = ""
    while operator not in ["*", "/", "+", "-", "multiply", "divide", "add", "subtract"]:
        operator = input("Which operation would you like to perform? OPTIONS: + (add)  - (subtract) * (multiply)  / (divide)")

    print(calculate(operator, x, y))

if __name__ == "__main__":
    main()
