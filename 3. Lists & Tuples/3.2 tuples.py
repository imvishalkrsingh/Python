# In Python, a tuple is a collection data type that
#  is similar to a list, but with one major difference: 
# tuples are immutable, meaning their elements cannot be
#  changed or modified after the tuple is created.
#  Tuples are defined using parentheses () and can
#  contain elements of different data types. 
# Here's a brief overview of tuples in Python:

# Creating Tuples:
my_tuple = (1, 2, 3, 4, 5)

# Accessing Elements:
# Elements of a tuple can be accessed using indexing, 
# similar to lists. Indexing starts from 0. 
# Negative indexing is also supported.

print(my_tuple[0])  # Output: 1
print(my_tuple[-1]) # Output: 5

# Immutable Nature:
# Once a tuple is created, you cannot modify its elements.
# This means you cannot add, remove, or change elements in a tuple.

my_tuple[0] = 10  # This will raise an error since tuples are immutable

# count():
# Syntax: tuple.count(value)
# Returns the number of occurrences of the specified value in the tuple.
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
print(count_of_2)  # Output: 3

# index():
# Syntax: tuple.index(value[, start[, end]])
# Returns the index of the first occurrence of the specified value in the tuple.
my_tuple = ('a', 'b', 'c', 'd', 'e')
index_of_c = my_tuple.index('c')
print(index_of_c)  # Output: 2

# These are the two main methods available for tuples. Unlike lists, there are no methods like append(), extend(), pop(), or clear() since tuples are immutable and do not support modification of their elements after creation.














