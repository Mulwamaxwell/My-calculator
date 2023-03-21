def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


print("Kindly choose your operation;")
print("1.Addition")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")
while True:
    choice = input("Enter your choice (1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = (input('your first number:'))
            num2 = (input('your second number:'))
        except ValueError:
            print("invalid number or numbers. Please insert a correct number.")
            continue
        if choice == "1":
            num1 = float(num1)
            num2 = float(num2)

            sum = num1 + num2

            print("The sum of", num1, "+", num2, "=", sum)

        elif choice == "2":
            num1 = float(num1)
            num2 = float(num2)

            print("{} - {}".format(num1, num2))
            print(num1 - num2)

        elif choice == "3":
            num1 = float(num1)
            num2 = float(num2)

            print("{} / {}".format(num1, num2))
            print(num1 / num2)

        elif choice == "4":
            num1 = float(num1)
            num2 = float(num2)

            print("{} * {}".format(num1, num2))
            print(num1 * num2)
        else:
            print("invalid numbers")

        continuation_of_calculation = input("Do you want to continue? (yes/no?):")

        if continuation_of_calculation == "no":
            break

        else:
            "yes"
            continue
