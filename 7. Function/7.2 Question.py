# Q1. WAP to print the length of a list.(List in the parameter)

def print_length(list):
    print(len(list))


cities = ["Delhi", "Noida", "Gurgaon", "Chennai", "Mumbai"]
print_length(cities)

# Q2. WAP to print the element of a list in a single line. (List in the parameter)

def print_list(list):
    
    for item in list:
        print(item, end = " ")

print_list(cities)

# Q3. WAP to print the factorial of n ( n is the parameter)

def cal_fact(n): 
    fact = 1

    for i in range(1, n+1):
        fact = fact * i

        print(fact)

cal_fact(5)

# Q4. WAP to convert USD to INR

def convert(usd):
    inr_value = usd * 83
    print(usd, "USD = ", inr_value, "INR")

convert(2)
