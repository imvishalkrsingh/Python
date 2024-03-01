# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.

movies = []
print("Enter first movies name : ")
mov1 = input()

print("Enter second movies name : ")
mov2 = input()

print("Enter third movies name : ")
mov3 = input()

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("Not Palindrome")



# WAP  to count the number of students with the "A" grade in the following tuple.

grade = ["C", "D","A", "A", "B", "B", "A"]

print(grade.count("A"))

# Store the above values in a list & store them from "A" to "D"
grade.sort()

print(grade)