# print('vishal singh')

# name = "vksingh"
# print(name)

# age = 23
# print(age)

# isAdult = True

# print("Hi " + name )

# old_age = input("Enter your old age : ")

# new_age = int(old_age)+2;

# print("Your New age is : " + str(new_age));


# name = "vishal singh"
# print(name.upper())


# age = 3
# if age >= 18 :
#     print("You are an adult")
#     print("You can Vote")

# elif age < 18 and age > 3 :
#     print("You are in school now")

# else :
#     print("You are Kid now")

# print("Thank you")


first = input("Enter first number :")

operator = input("Enter Operator (+,-,*,/,%) : ")

second = input("Enter second number : ")

if operator == "+" :
    sum = int(first) + int(second)
    print(sum)

elif operator == "-" :
    print(int(first) - int(second))

elif operator == "*" :
    print(int(first) * int(second))

elif operator == "/" :
    print(int(first) // int(second))

elif operator == "%" :
    print(int(first) % int(second))

else : 
    print("Invalid Operator ")