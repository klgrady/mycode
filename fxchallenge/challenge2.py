#!/usr/bin/python3

def calculate(operator, x, y):
    if operator == "*": return x * y
    if operator == "/":
        if y != 0.0: return x / y
        return "Not a Number (can't divide by zero, bro)"
    if operator == "+": return x + y
    if operator == "-": return x - y

def main():
    arithmetic_list = input("Enter a simple arithmetic statement with spaces between numbers and operator (e.g. 2 * 2) ").strip().split(' ')
    try:
        x, operator, y = [float(arithmetic_list[0]), arithmetic_list[1], float(arithmetic_list[2])]
        if operator not in ["+", "-", "*", "/"]: raise Exception
        print(calculate(operator, x, y))
    except:
        print("Sorry, you need to enter a simple arithmetic statement with spaces, like '2 * 2'. Since you can't follow directions, you get nothing.")

if __name__ == "__main__":
    main()
