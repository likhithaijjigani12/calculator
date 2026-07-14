import math


def display_menu():
    print("\n*** CALCULATOR ***")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")


# --- Operation Functions ---

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


def power(base, exponent):
    return base ** exponent


def square(a):
    return a ** 2


def square_root(a):
    if a < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(a)


def factorial(a):
    if a < 0:
        return "Error: Factorial is not defined for negative numbers."
    if not float(a).is_integer():
        return "Error: Factorial is only defined for integers."
    return math.factorial(int(a))


# --- Main Program Loop ---

def calculator():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ").strip()

        if choice == '10':
            print("Goodbye! Thanks for using the calculator.")
            break

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid choice! Please enter a number between 1 and 10.")
            continue

        try:
            # Operations requiring two inputs
            if choice in ['1', '2', '3', '4', '5', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {result}" if isinstance(result, str) else f"Result: {num1} / {num2} = {result}")
                elif choice == '5':
                    result = modulus(num1, num2)
                    print(f"Result: {result}" if isinstance(result, str) else f"Result: {num1} % {num2} = {result}")
                elif choice == '6':
                    print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")

            # Operations requiring one input
            elif choice in ['7', '8', '9']:
                num = float(input("Enter number: "))

                if choice == '7':
                    print(f"Result: {num}^2 = {square(num)}")
                elif choice == '8':
                    result = square_root(num)
                    print(f"Result: {result}" if isinstance(result, str) else f"Result: {num} = {result}")
                elif choice == '9':
                    result = factorial(num)
                    print(f"Result: {result}" if isinstance(result, str) else f"Result: {int(num)}! = {result}")

        except ValueError:
            print("Invalid input! Please enter valid numeric values.")


# Run the calculator
if __name__ == "__main__":
    calculator()