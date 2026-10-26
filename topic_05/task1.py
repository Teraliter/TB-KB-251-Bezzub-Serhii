import random

options = ["stone", "scissor", "paper"]
wins_over = {"stone": "scissor", "scissor": "paper", "paper": "stone"}

user_choice = input("Enter stone, scissor or paper: ").strip().lower()

if user_choice not in options:
    print("Invalid choice")
else:
    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Draw")
    elif wins_over[user_choice] == computer_choice:
        print("You win")
    else:
        print("Computer wins")
