# Taking input for A and G as strings
A_input = input("A : ")
G_input = input("G : ")

# Converting A to integer
A = int(A_input)

# Checking the value of G and processing accordingly
if (A == 1 or A ==2 and G_input == "M"):
    print("Fee is 100")

elif (A == 3 or A == 4 and G_input == "F"):
    print("Fee is 200")

elif (A == 5 and G_input == "M"):
    print("Fee is 300")

else:
    print("No Fee")
