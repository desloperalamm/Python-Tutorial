# Question 1: Write a Python program to calculate the sum and average of a list of numbers.
# ========================================================================================

# my_list = [10, 20, 30, 40, 50]
# sum = 0
# for i in my_list:
#     sum += i
# print("Sum:", sum)
# print(f"Average is: {sum / len(my_list)}")


# my_list = [10,20,30,40,50,60,70]
# sum = 0
# # average = 0
# for i in my_list:
#     sum += i

# print(f"Sum is: {sum} && Average is: {sum / len(my_list)}")


# Question 2: WAP to find Maximum element with index
# ==================================================

# my_list = [10, 20, 30, 40, 70, 25, 5, 60, 15]

# max_value = my_list[0]
# max_index = 0

# for i in range(len(my_list)):
#     if my_list[i] > max_value:
#         max_value = my_list[i]
#         max_index = i

# print(f"Maximum value is: {max_value} at index {max_index}")



# # Question 3: WAP to find Second Minimum element with index
# # =========================================================

# my_list = [10,20,30,25,5,60,40,15,70]

# max_value = my_list[0]
# max_value2 = my_list[0]
# max_index = 0
# max_index2 = 0

# for i in range(len(my_list)):
#     if my_list[i] > max_value:
#         max_value2 = max_value
#         max_value = my_list[i]
#         max_index2 = max_index
#         max_index = i
# print(f"first max value is: {max_value} at index {max_index} && second max value is: {max_value2} at index {max_index2}")



# # Question 4: WAP to cheeck a list is sorted or not
# # =========================================================

# my_list = [10, 9, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in range(len(my_list)-1):
#     if my_list[i] < my_list[i+1]:
#         continue
#     else:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")




# # Question 5: WAP to left rotate a list by 1 elements
# # =========================================================

# my_list = [10, 20, 30, 40, 50]

# for i in range(len(my_list)-1):
#     my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

# print("Left rotated list is:", my_list)


# # Question 6: WAP to left rotate a list by k elements
# # =========================================================

# k = int(input("Enter the number of positions to left rotate: "))
# my_list = [10, 20, 30, 40, 50, 60, 70]

# for i in range(k):
#     for i in range(len(my_list)-1):
#         my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

# print("Left rotated list is:", my_list)


# # Question 7: WAP to reverse a list without using extra space
# # =========================================================

my_list = [10, 20, 30, 40, 50,60]
reversed = len(my_list) - 1

for i in range(len(my_list)//2):
    my_list[i], my_list[reversed] = my_list[reversed], my_list[i]
    reversed -= 1

print("Reversed list is:", my_list)








# my_list = [10, 20, 30, 40, 79, 70, 25, 5, 80, 15]

# max_value = my_list[0]
# max_value2 = my_list[0]
# max_value3 = my_list[0]
# max_index = 0
# max_index2 = 0
# max_index3 = 0

# for i in range(len(my_list)):
#     if my_list[i] > max_value:
#         max_value3 = max_value2
#         max_value2 = max_value
#         max_value = my_list[i]
#         max_index3 = max_index2
#         max_index2 = max_index
#         max_index = i

#     elif my_list[i] > max_value2 and my_list[i] != max_value:
#          max_value3 = max_value2
#          max_value2 = my_list[i]

# print(f"first maximum Value is: {max_value} at index {max_index} && second maximum Value is: {max_value2} at index {max_index2} && third maximum Value is: {max_value3} at index {max_index3}") 