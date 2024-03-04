# Create a new file "practice.txt" using python add the following data in it.
# Hi everyone,
# We are learning file I/O
# Using java
# I like programming in java

# Q1. WAF that replaces all occurences of "java" with "Python" in above file.

def check_for_words():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("java", "Python")
    print(new_data)

check_for_words()