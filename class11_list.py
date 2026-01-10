# Question 1: Write a Python program to calculate the sum and average of a list of numbers.
# ========================================================================================

# my_list = [10, 20, 30, 40, 50]
# sum = 0
# for i in my_list:
#     sum += i
# print("Sum:", sum)
# print(f"Average is: {sum / len(my_list)}")


# Question 2: Maximum element with index
# ======================================

my_list = [10, 20, 30, 40, 70, 25, 5, 60, 15]

max_value = my_list[0]
max_index = 0

for i in range(len(my_list)):
    if my_list[i] > max_value:
        max_value = my_list[i]
        max_index = i

print("maximum value is: ", max_value)
print("index of maximum value is: ", max_index)


# max_value = my_list[0]
# max_index = 0

# for i in range(1,len(my_list)):
#     if my_list[i] > max_value:
#         max_value = my_list[i]
#         max_index = i

# print("Maximum value is:", max_value)
# print("Index of maximum value is:", max_index)