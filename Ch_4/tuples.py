# Chapter 4, Tuples

# Python refers to values that cannot change as 'immutable', and an immutable list is called a 'tuple' 
# Creating a tuple is easy, just put items in (), not in []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# NOTE: To make a tuple with only one element, put a comma after the only item

dimensionado = (123,)
print(dimensionado[0])

# Loops can be used with tuples

print("\nLoop list")
for dimension in dimensions:
    print(dimension)

# While tuples cannot be changed, they can be overwritten (simply assign them anew)

print("\nOriginal tuple:")
dimensions = (5, 10)
for dimension in dimensions:
    print(dimension)

print("\nModified tuple:")
dimensions = (99, 77)
for dimension in dimensions:
    print(dimension)


# LONG CODE TEST

superlist = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', \
    'test8']
print(superlist)