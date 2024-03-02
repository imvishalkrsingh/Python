# Q1. Print numbers from 1 to 100.
count = 1
while count <= 100:
    print(count)
    count = count + 1

# Q2. Print numbers from 100 to 1.
count1 = 100
while count1 >= 1:
    print(count1)
    count1 = count1 - 1

# Q3. Print the multiplication table of a number n.
n = int(input("Enter a number: "))
table = 1
while table <= 10:
    print(n, "*", table, " = ", n * table)
    table = table + 1

# Q4. Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# Q5. Search for a number x in this tuple using a loop
# Tuple is used instead of list in the description
tuple_numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
index = 0
while index < len(tuple_numbers):
    if x == tuple_numbers[index]:
        print(f"{x} found at index: {index}")
        break  # Once found, we can stop searching
    index += 1
