# Define a list of marks
marks = [94.4, 87.5, 95.2, 66.4, 45.1]

# Print the list of marks
print(marks)

# Print the type of the variable marks
print(type(marks))

# Print the length of the marks list
print(len(marks))

# Access and print the first element of the marks list
print(marks[0])

# Access and print the second element of the marks list
print(marks[1])

# Define a list representing a student
student = ["vishal", 99.9, 24, "Delhi"]

# Modify the first element of the student list
student[0] = "Vishal singh"

# Print the modified student list
print(student)

# Define a list representing scores
score = [87, 64, 33, 95, 76]

# List slicing examples
# Slicing from index 1 to 3 (exclusive) of the score list
print(score[1:4])  # Output: [64, 33, 95]

# Slicing from the beginning to index 1 of the score list
print(score[:1])   # Output: [87]

# Slicing from index 1 to the end of the score list
print(score[1:])   # Output: [64, 33, 95, 76]

# Slicing from the third last element to the second last element of the score list
print(score[-3:-1])  # Output: [33, 95]


# list methods

list = [2, 1, 3]

list.append(4)  # add one element at the end [2,1,3,4]
print("After append", list)

list.sort() # sorts in ascending order [1,2,3]
print("After sort", list)

list.sort(reverse=True)  #sorts in descending order [3,2,1]
print("After sort desc :", list)

list.reverse() #reverse list [3, 1, 2]
print("After reverse", list)

# list.insert(idx, el)
list.insert(2,55)
print("After insert", list)

list.remove(1)  #removes first occurrence of element [2,3,1]
print("After remove", list)

my_list = [10, 20, 30, 40]
popped_element = my_list.pop(1)  # Removes and returns the element at index 1 (20)
print(popped_element)  # Output: 20
print(my_list)  # Output: [10, 30, 40]

my_list = [10, 20, 30, 40]
my_list.clear()  # Clears all elements from the list
print(my_list)  # Output: []

my_list = [10, 20, 30, 20, 40, 20]
count_of_20 = my_list.count(20)  # Counts occurrences of 20
print(count_of_20)  # Output: 3

my_list = [10, 20, 30]
new_list = my_list.copy()  # Creates a copy of my_list
print(new_list)  # Output: [10, 20, 30]


my_list = [10, 20, 30]
another_list = [40, 50]
my_list.extend(another_list)  # Extends my_list with elements from another_list
print(my_list)  # Output: [10, 20, 30, 40, 50]

my_list = [10, 20, 30, 20, 40, 20]
index_of_20 = my_list.index(20)  # Finds the index of the first occurrence of 20
print(index_of_20)  # Output: 1


