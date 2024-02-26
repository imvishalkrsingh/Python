# Strings and Numeric values can operate together with *
a = 2
b = 3
Txt = "@"
print(a * Txt * b)

# String & String can operate with + 

a = "2"
b = 3
Txt1 = "@"

print((a + Txt) * b)

# Numeric values can operate with all arithmetic operators

a = 10
b = 5
c = 4
print(a+b*c)

# Arithmetic expression with integer and float will result in float

a = 10
b = 5.0
c = a*b
print(c)

# Result of division operator with two integers will be float
a = 1
b = 2
c = a/b
print(c)

# integer division with flaot and int will give int displayed as float

a = 1.5
b = 3
c = a // b
print(c, a/b)

# floor gives closest integer, which is lesser than or equal to the float value
# Result of (A // B) is same as floor (A / B)

a = 12
b = 5
c = a//b
print(c)

a = -12
b = 5
c = a//b
print(c, a/b)

a = 12
b = -5
c = a//b
print(c, a/b)



# Remainder is negative when denominator is negative
a = -5
b = 2
c = a % b
print(c)

a = 5
b = 2
c = a % b
print(c)

a = 5
b = -2
c = a % b
print(c)

name = input("Enter your name : ")
print(name)

age = int(input("Enter your age : "))
print(age)