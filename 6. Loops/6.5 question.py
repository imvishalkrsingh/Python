# Using for loop 
# print the elements of the following list using a loop : 
# [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]

for val in list:
    print(val)
else:
    print("Finished")

# Q2. Search for a number x in this tuple using loop :
    
list1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49
idx = 0
for el in list1:
    if el == x:
        print("Element found at idx:", idx)
    idx += 1

# Range() in Loop
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
# Printing numbers from 0 to 5 using a for loop
    
for x in range(6):
    print(x)

# Printing numbers from 2 to 9 using a for loop with range(start, stop)
for i in range(2, 10):
    print(i)

# Printing even numbers from 2 to 8 using a for loop with range(start, stop, step)
for i in range(2, 10, 2):
    print(i)

# Print even numbers from 2 to 40
print("Even numbers from 2 to 40:")
for i in range(2, 41, 2):
    print(i)

# Print odd numbers from 1 to 29
print("Odd numbers from 1 to 29:")
for i in range(1, 30, 2):
    print(i)

# Print numbers from 1 to 10
print("Print: 1 to 10")
for i in range(1, 11):
    print(i)

# Print numbers from 100 to 10 in steps of -10
print("Print: 100 to 10")
for i in range(100, 0, -10):
    print(i)

# Print multiplication table for a given number
n = int(input("Enter a number: "))
print("Multiplication table for", n, ":")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Prompting the user to enter the value of N
num = int(input("Enter value of N: "))

# Initializing the variable to store the sum
sum = 0

# Looping through the numbers from N to 1 and finding their sum
while num >= 1:
    sum = sum + num  # Accumulating the sum
    num -= 1         # Decrementing num in each iteration

# Printing the sum
print("The sum of the first", num, "numbers is:", sum)

# using for loop

numb = 5
for i in range(1, num+1):
    sum = sum + i
    print("Total sum : ", sum)

