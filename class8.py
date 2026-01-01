# =================================== Question 1st
# print each digit (Reverse Order)
# break a number  into individual digit and print them string from the last digit

# a = int(input("Enter a number: which you want to reverse: "))

# while a > 0:
#     print (a % 10)
#     a =  a // 10




# ======================================== Question 2nd
# Sum of Digits
# Add all the digits of a number (e.g. 123 > 1+2+3=6).

# a = int(input("Enter a number: "))
# sum = 0
# while a > 0:
#     sum += a % 10
#     a = a // 10
# print(f"The sum of digits is {sum}")



# ======================================== Question 3rd
# Reverse a Number
# Input a number and reverse its digit

# a = int(input("Enter a number: "))
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(f"The reverse is {rev}")



# ======================================== Question 4th
# Palindrome Number
# Input a number and check if it is a palindrome or not

# a = int(input("Enter a number: "))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if rev == copy:
#     print("It is a palindrome Number")

# else:
#     print("It is not a palindrome Number")



# ======================================== Question 5th
# Automorphic Number
# Input a number and check if it is an automorphic number or not

a = int(input("Enter a number which you wants to check: "))
dupl = a
square = a ** 2

count = 0
while a > 0:
    count += 1
    a = a // 10

extract = square % (10**count)

if extract == dupl:
    print("It is an automorphic number")

else:
    print("It is not an aotumorphic number")