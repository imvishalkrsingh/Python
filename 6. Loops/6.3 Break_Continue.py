# In Python, the break statement is used to exit or terminate the current loop prematurely, regardless of whether the loop's condition is still true or not. When Python encounters a break statement inside a loop, it immediately exits the loop, and the control of the program moves to the statement immediately following the loop.

# Example: Using break in a while loop
count = 0
while True:  # Infinite loop
    print(count)
    count += 1
    if count >= 15:
        break  # Exit the loop when count is equal to or greater than 5

# Note - Break keyword is used to terminate the loop when encountered.

    
# Example: Using continue in a while loop

count = 0
while count < 5:  # Loop until count reaches 5
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop body if count is 3
    print(count)
    
# Note - Continue keyword is used to terminates execution in the current iteration & continues execution of the loop with the next iteration.
