# Get input from the user
n = int(input("Enter a positive integer : "))

# Initialize sum
sum = 0

# Calculate sum of natural numbers
for i in range(1, n + 1):
    sum += i

# Display the result
print(f"The sum of the first {n} natural numbers is : {sum}")
