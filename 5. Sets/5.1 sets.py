# sets is the collection of the unordered items.
# Each element in the set must be unique & immutable.

set = { 1,2,2,2}

# Repeated elements stored only once, so it resolved to {1,2}
print(set)

Collection = {1,2,3,4}
print(Collection)

print(type(Collection))

# my_set = set()  # empty set syntax
# print(my_set)


# Set Methods

set1 = { 1,2,3,4,5}

set1.add(2) #adds an element
print("After add : ")
print(set1)

set1.remove(2) #removes the element
print("After remove : ")
print(set1)

set1.pop()   #removes a random value
print("After POP : ")
print(set1)

set1.clear() #empties the set
print("After clear : ")
print(set1)

# Sets and Union

set3 = {5, 6, 7, 8}
set4 = {10, 9, 8, 7}

# union method -- Combines both set values & return new
new1 = set3.union(set4)
print(new1)

# Intersection method -- Combines common values & return new
new2 = set3.intersection(set4)
print(new2)








