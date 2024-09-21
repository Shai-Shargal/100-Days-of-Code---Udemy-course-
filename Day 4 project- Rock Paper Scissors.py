import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

# Prompt user for input
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")

# Ensure user inputs a valid number
while choice not in ['0', '1', '2']:
    choice = input("Invalid choice. Please type 0 for Rock, 1 for Paper, or 2 for Scissors: ")

# Convert choice to integer
choice = int(choice)

# Print user's choice
print(f"You chose:\n{game[choice]}")

# Computer's choice
computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{game[computer_choice]}")

# Determine winner
if choice == computer_choice:
    print("It's a tie!")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
