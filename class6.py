#  Conditional statements
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# age  = int(input("enter your age:"))
# if age >= 18:
#     print("you are elder")

# else:
#     print("you are child")


# paisa = int(input("enter your paisa:"))

# if paisa == 50:
#     print("I can eat only veg biryani")

# elif paisa == 100:
#     print("I can eat only biryani")

# else:
#     print("I can eat chicken changezi")


# question 1st
#  check which number is greater

# a = float(input("enter first number:"))
# b = float(input("enter second number:"))

# if a > b:
#     print(f"{a} is greater than {b}")

# elif a < b:
#     print(f"{b} is greater than {a}")

# else:
#     print(f"{a} and {b} both are equal") 


# ======================== Question 2nd and 3rd
# ======================== Greet by gender and Greeting by case sensitive

# gender = input("enter your gender:")

# if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
#     print("Good Morning Sir")

# elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
#     print("Good Morning Ma'am")
# else:
#     print("Please enter a valid gender")


# ======================== Question 4th
# ======================== check user number is even or odd

# number = int(input("enter a number:"))

# if number % 2 == 0:
#     print(f"{number} is even")

# else:
#     print(f"{number} is odd")


# ======================== Question 5th
# ======================== check a person is eligible to vote or not

# name = input("enter your name: ")
# age = int(input("enter your age: "))

# if age >=18:
#     print(f"{name} is eligible to vote")

# else:
#     print(f"{name} is not eligible to vote. \nAfter {18-age} you will be eligible to vote")


# ======================== Question 6th
# ======================== check a Days of week checker

# day = int(input("enter a number:"))
# day = day % 7

# if day == 1:
#     print("Sunday")

# elif day == 2:
#     print("Monday")

# elif day == 3:
#     print("Tuesday")

# elif day == 4:
#     print("Wednesday")

# elif day == 5:
#     print("Thursday")

# elif day == 6:
#     print("Friday")

# elif day == 7:
#     print("Saturday")

# else:
#     print("Please enter a valid number")


# Question 7th
# ======================== check a number three number is equal or not and check which number is greater

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))

# if a == b and b == c:
#     print("All numbers are equal")

# elif a == b or b == c or c == a:
#     print("Two numbers are equal")

# elif a > b and a > c:
#     print(f"{a} is greater than {b} and {c}")

# elif b > a and b > c:
#     print(f"{b} is greater than {a} and {c}")

# else:
#     print(f"{c} is greater than {a} and {b}")



# Qustion 8th
# ======================== check a leap year or not with century

# year = int(input("Enter a year: "))

# if year % 100 == 0 and year % 400 == 0:
#      print(f"{year} is a leap year")

# elif year % 100 != 0 and year % 4 == 0:
#      print(f"{year} is a leap year")

# else:
#      print(f"{year} is not a leap year")


# Question 9th
# ======================== give discount to a person on his total bill amount

# bill = int(input("Enter your total bill amount: "))

# if bill >= 1000 and bill <= 4999:
#     print(f"Your total bill amount is {bill} and you will get 10% discount and your total bill is {(bill*90)/100}")

# elif bill >= 5000:
#     print(f"Your total bill amount is {bill} and you will get 20% discount and your total bill is {(bill*80)/100}")

# else:
#     print(f"Your total bill amount is {bill} and you will not get any discount and your total bill is {bill}")


# Question  10th
# ======================== check character is vowel or consonant

char = input("Enter a Character:")

if char in "aeiouAEIOU":
    print(f"{char} is a vowel")

else:
    print(f"{char} is a consonant")