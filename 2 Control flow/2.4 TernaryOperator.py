# Single line if / Ternary Operator

# <var> = <val1> if <condition> else <var2>

food = input("Food : ")
eat = "Yes" if food == "veg" else "No"
print("Decision of Eat : ", eat)

print("Decision of Eat : ", "Yes" if input("Food : ") == "cake" else "No")


age = int(input("Age : "))
vote = "Yes" if age >= 18 else "No"
print(vote)
