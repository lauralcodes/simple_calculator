# addition
def add(a, b):
    return a + b


# substraction
def subtract(a, b):
    return a - b

# multiplication
def multiply(a, b):
    return a * b


# division
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")


# power
def power(a, b):
    return a ** b


# remainder
def remainder(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")

while True:    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Remainder")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid input. Please select a valid option.")
        continue


    print(f"You selected option {choice}.")

    if choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        while True:
            num1 = (input("Enter first number: "))
            try:
                num1 = float(num1)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            num2 = (input("Enter second number: "))
            try:
                num2 = float(num2)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        


        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        else:
            try:
                print(f"{num1} % {num2} = {remainder(num1, num2)}")
            except ValueError as e:
                print(e)


        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break
        