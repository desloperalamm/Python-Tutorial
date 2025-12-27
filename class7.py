# class 7th
# =================== loops ==================

# for i in range(10,41,1):
#     print("hello python",i)

# for i in range(-10,21,1):
#     print(i)

# for i in range(35,4,-1):
#     print(i)


# =================== print table by coder
# for i in range(5,51,5):
#     print(i)

# =================== print table by user input

# n = int(input("Enter a number: "))

# for i in range(n,(n*10)+1,n):
#     print(i)

# s = "Hello welcome to python"

# for i in range(0,len(s),1):
#     print(s[i])



# ==================================================================================================================
# ==================================================================================================================

# Question 1st
# ======================== n number print by user input

# n = int(input("Enter a number:"))

# for i in range(1,n+1):
#     print("Hello World", i)



# Question 2nd
# ======================== print 1 number to n number print by user input

# n = int(input("Enter a number:"))

# for i in range(1,n+1):
#     print(i)



# Question 3rd
# ======================== print n number to 1 number print by user input

# n = int(input("Enter a number:"))

# for i in range(n,0,-1):
#     print(i)



# Question 4th
# ======================== sum of natural number by user input

# n = int(input("Enter a number:"))

# sum = 0

# for i in range(1,n+1):
#     sum += i
# print(f"the sum is {sum}")



# Question 5th
# ======================== factorial of a number by user input

# n = int(input("Which number you want factorial:"))

# fact = 1

# for i in range(1,n+1):
#     fact *= i

# print(f"the factorial of {n} is {fact}")



# Question 6th
# ======================== n number sum but even_sum alag and odd_sum alag

n = int(input("Enter a number:"))

even_sum = 0
odd_sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"the even sum is {even_sum} and the odd sum is {odd_sum}")