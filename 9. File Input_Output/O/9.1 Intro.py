# Python can be used to perform operations on a file. (Read and Write data)

# Types of all files
# 1.Text files : .txt, .docx, .log etc
# 2.Binary files : .mp4, .mov, .png, .jpg etc

# Open, read and close files 
# We have to open a file before reading or writing

# f = open("file_name", "mode") -- f = open("sample.txt", "r")

# data = f.read()
# f.close()

# Example: Opening and reading from a file
# We have a file demo.txt to open 

f = open("demo.txt", "r")  # Open file in read mode

data = f.read()  # Read entire content of file into data

print(data)  # Print the contents of the file

print(type(data))  # Print the type of data (str)

# Reading file line by line
line1 = f.readline()  # Read the first line
print(line1)

line2 = f.readline()  # Read the second line
print(line2)

line3 = f.readline()  # Read the third line
print(line3)

f.close()  # Close the file


# Writing to a file
# We have a file demo.txt in which we want to write 

f = open("demo.txt", "w")  # Open file in write mode

f.write(" I want to learn Javascript tomorrow")  # Write content to the file

f.open("demo.txt", "a")  # This line is not necessary

f.close()  # Close the file



# 'With' Syntax
# Using 'with' statement ensures the file is properly closed after usage

# with open ("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# Uncommented and corrected version:
# with open("demo.txt", "r") as f:  # Open file in read mode using 'with' statement
#     data = f.read()  # Read entire content of file into data
#     print(data)  # Print the contents of the file


# Deleting a file -- Using the OS module

# Module (Like a code library) is a file written by another programmer that generally has a function we can use :--
    
# import os
# os.remove("demo.txt")

# This code imports the os module and uses its remove function to delete the file named "demo.txt"
