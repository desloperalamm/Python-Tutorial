import random

# num = random.randint(1,100)

# tries = 0

# while True:
#     guessed = int(input("Enter a number between 1 and 100: "))
#     tries += 1
#     if guessed == num:
#         print(f"You guessed the number in {tries} tries!")
#         break
#     elif guessed > num:
#         print("Please guess a smaller number.\n")
#     else:
#         print("please guess a larger number.\n")  

# ===================================================== game 2

# stone paper scissors

# user = input("Enter your choice (stone, paper, scissors): ")
# computer = random.choice(["stone", "paper", "scissors"])

user = int(input("Enter your choice (1 for stone, 2 for paper, 3 for scissors): "))
computer = random.randint(1,3)

if user == 1 and computer == 3:
    print("You win! Stone crushes scissors.")
elif user == 2 and computer == 1:
    print("You win! Paper covers stone.")
elif user == 3 and computer == 2:
    print("You win! Scissors cut paper.")
elif user == computer:
    print("It's a tie!")
else:
    print("Computer wins!")