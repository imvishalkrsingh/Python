# Prompting the user to enter the number
num = int(input("Enter a number: "))

# Initializing the factorial variable
factorial = 1

# Calculating factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i

    # Printing the factorial
    print("The factorial of", num, "is", factorial)
