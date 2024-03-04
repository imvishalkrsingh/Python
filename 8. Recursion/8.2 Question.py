# Write a recursive function to print all elements in a list. (Hint : Use list and index as parameter)


def print_all(listt, idx):
    if idx == len(listt):
        return
    
    print(listt[idx])
    print_all(listt, idx+1)

fruits = ["apple", "banana", "guava", "grapes"]
print_all(fruits, 0)


# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==0):
        return 0
    
    return sum(n-1)+n

sum1 = sum(5)
print(sum1)