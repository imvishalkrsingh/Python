# Get input from the user
num = int(input("Enter a non-negative integer: "))

# Initialize factorial
factorial = 1

# Calculate factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)
