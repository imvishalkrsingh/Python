# String is a data type that stores sequence of character

# Basic operations : 
# Concatenation : "hello" + "World" = "helloworld"

fname = "vishal"
lname = "Singh"
fullName = fname + lname
print(fullName)

# length of str : len(str)

str1 = "Vishal"
len1 = len(str1)

print(len1)


str2 = "Singh"
len2 = len(str2)

print(len2)

str1 = "This is a String."

# for next line : "\n"
# for tab : "\t"
# for single quote : "\'"
# for double quote : "\'"

# String Functions

str = "I am a coder."

str.endswith("er.") #return true if string ends with substr

str.capitalize() #capitalize 1st char

str2 = str.replace("am", "was")  #replaces all occurances of old with new

str.find("a") #returns 1st index of 1st occurence
print(str2)

str.count("am") #counts the occurrence of substr in string





