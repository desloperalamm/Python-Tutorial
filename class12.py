# # tuple has hytrogenius nature

# tuple = (10,20,30,40,50,60,70,80,90,100)
# print(type(tuple))
# print(tuple)


# # tuple has immutable nature

# tuple = (10,20,10,10,20,20,30,40,50)
# print(tuple)


# # we can't change value of tuple

# tuple = (10,20,30,40,50)
# tuple[2] = 100  # TypeError: 'tuple' object does not support item assignment
# print(tuple)


# # tuple unpaking
# tuple = (10,20,30)
# a, b, c = tuple # tuple unpaking
# print(tuple)
# print(a, b, c)




# # Tuple traversing

# tuple = (10,20,30,40,50)
# # 1st way
# for i in tuple:
#     print(i)

# # 2nd way
# for i in range(len(tuple)):
#     # print(tuple[i])
#     print(i, ":", tuple[i])




# # Tuple methods
# # tuple has only two methods count() and index()

# 1st method count()

# tuple = (10,20,10,10,20,20,30,40,50,10)
# print(tuple.count(10))  # output 4

# tuple = (10,20,30,40,50)
# print(tuple.index(30)) #Output 2

# 2nd method index()

tuple = (10,20,30,40,50)
print(tuple.index(20)) #Output 1


print(tuple.index(100)) #ValueError: tuple.index(x): x not in tuple