import random

list = ["rock", "paper", "scissors"]
choice = input("Rock, Paper or Scissors: \n")
botChoice = random.choice(list)

choice = choice.lower()
if choice in list:
    print("\nYou picked: %s" % choice)
    print("The bot picked: %s" % botChoice)
else:
    print("Please enter a valid option!")

# outcomes
if choice == botChoice:
    print("It's a draw, you both picked %s" % choice + "!")
elif choice == "rock" and botChoice == "paper":
    print("The bot won, better luck next time!")
elif choice == "paper" and botChoice == "rock":
    print("You won, congratulations!")
elif choice == "rock" and botChoice == "scissors":
    print("You won, congratulations!")
elif choice == "scissors" and botChoice == "rock":
    print("The bot won, better luck next time!")
elif choice == "scissors" and botChoice == "paper":
    print("You won, congratulations!")
elif choice == "paper" and botChoice == "scissors":
    print("The bot won, better luck next time!")
