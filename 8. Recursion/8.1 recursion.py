# When a function call itself repeatedly

#  Q1. Print n to 1 backwards

def show(n):
    if(n == 0):
        return
    
    print(n)
    show(n-1)

show(5)

# Q2. Factorial of a number 

def fact (n):
    if n == 0 or n == 1:
        return 1
    
    else : return n * fact(n-1)

print("Factorial is", fact(5))


# Q3. Write a recursive function to print all elements in a list. (Hint - use list and index as parameter)

def print_list_recursive(data, index=0):
  if index == len(data):
    return

  print(data[index])
  print_list_recursive(data, index + 1)

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_recursive(my_list)