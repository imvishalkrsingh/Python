# Block of statements that perform a specific task.

# def fun_name(param1, param2,....):
    # some work
    # return value

# function_name(argu1, argu2) ----- function call

# Repeat = Redundant

def cal_sum(a, b):
    sum = a + b
    print(sum)

cal_sum(2,3)


def cal_avg(a,b,c):
    
    avg = (a + b + c) / 3

    print(avg)

cal_avg(1,2,3)

# Types of Function in Python
# 1. Built in function -- print(), len(), type(), range()
# 2. User-defined Function -- The function defined by the users is called user-defined function

# to print in a same line 
print("Vishal kumar", end = " ")
print("singh")

# Default function

def cal_prod(a, b=2):
    print(a*b)
    return (a*b)

cal_prod(2)




