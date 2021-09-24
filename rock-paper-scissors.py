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

import random 

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("Your choice: \n")
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("You entered an invalid number!")
print("Computer's choice: \n")
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else: 
  print(scissors)

if choice == 0:
  if computer_choice == 0:
    print("You're even")
  elif computer_choice == 1:
    print("Computer won")
  else:
    print("You won")
elif choice == 1:
  if computer_choice == 0:
    print("You won")
  elif computer_choice == 1:
    print("You're even")
  else:
    print("Computer won")
elif choice == 2:
  if computer_choice == 0:
    print("Computer won")
  elif computer_choice == 1:
    print("You won")
  else:
    print("You're even")
else:
  print("You entered an invalid choice!")