# store following word meanings in a python dictionary : 
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}

print(dict)

# You are given a list of subjects for students.
# Assume one classroom is required for 1 subject. 
# How many classrooms are needed by all students.

"python", "java", "C++", "Python", "Javascript",
"Java", "Python", "Java", "C++", "C"

subjects = {
    "Python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}

print(subjects)
print(type(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary and add one by one. 
# Use subject name as key and marks as value.

marks = {}

x = int(input("Enter phy : "))
marks.update({"phy" : x})

x = int(input("Enter math : "))
marks.update({"math" : x})

x = int(input("Enter chem : "))
marks.update({"chem" : x})

print(marks)
print(type(marks))

# figure out a way to store 9 & 9.0 as separate values in the set (You can take help of built-in data types)

# Create two sets, one for integers and one for floats

# Create a set with string representations of the values
values_set = {'9', '9.0'}

print(values_set)  # Output: {'9', '9.0'}

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)


