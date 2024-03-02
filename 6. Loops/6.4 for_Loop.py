# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


list = [1,2,3,4,5,6,7]

for val in list:
    print(val)


name = "Vishal kumar singh"

for chr in name :
    print(chr)
else:
    print("Finally finished!")

    
# Loops are used for sequential traversal. for traversing list, string, tuples etc

# Range() in Loop
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

    seq = range(5)
    print(seq)

# Pass statements -- Pass is a null statement that does nothing. It is used as a placeholder for future code.
    
    for i in range(5):
        pass

    print("Some important work")