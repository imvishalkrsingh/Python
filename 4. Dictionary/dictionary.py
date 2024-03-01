# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) and don't allow duplicate keys

dict = {
    "name" : "vishal",
    "cgpa" : 9.6,
    "marks": [98,97,95],
    "age" : 35,
    "is_adult" : True,
    "Subject" : ["Python", "Java", "C"],
    "topics" : ("dictionary", "Set"),
    10 : 100,
    12.95 : 98.9,
}

# Reassign

dict["name"] =  "Vishal Kumar Singh"
dict["age"] = 24


print(dict)

# Null dictionaries

null_dict = {}

null_dict["New"] = "V.K.SINGH"
print(null_dict)

# Nested Dictionaries
student = {
    "name": "vishal",
    "subject": {
        "physics": 98,
        "chemistry": 97,
        "math": 99,
    }
}

print(student)

print(student["subject"]["chemistry"])

# Method to find keys 
print(student.keys())

# typecast from dictionary to list
print(list(student["subject"]))

# Method to find length of keys 
print(len(student))
print(len(list(student["subject"])))

# values in dictionary
print(student.values())

# items in dictionary
print(dict.values())

# update method in dictionary

new_dict = {"name" : "aman kumar", "age" : 20}

student.update(new_dict)

print(student)
