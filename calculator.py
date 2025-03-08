def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Select an operation (1-5): "))
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"The result is: {add(num1, num2)}")
            elif choice == 2:
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == 4:
                try:
                    print(f"The result is: {divide(num1, num2)}")
                except ValueError as e:
                    print(e)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()