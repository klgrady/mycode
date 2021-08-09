#!/usr/bin/python3

def main():
    fizzes, buzzes, fizzbuzzes = [0, 0, 0];
    with open('numfile.txt') as file:
        for num in file.readlines():
            if (int(num) & 5 == 0 and int(num) % 3 == 0): print("FizzBuzz", end=""); fizzbuzzes += 1
            elif (int(num) % 3 == 0): print("Fizz", end=""); fizzes += 1
            elif (int(num) % 5 == 0): print("Buzz", end=""); buzzes += 1
            else: print(num.strip(), end="")
            print(" ", end="")
    print(f"\nFizzes: {fizzes}   Buzzes: {buzzes}   FizzBuzzes: {fizzbuzzes}")

if __name__ == "__main__":
    main()
