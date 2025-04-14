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
images = [rock, paper, scissors]

user_pick = int(input("Pick a number: 0 for rock, 1 for paper or 2 for scissors"))
if user_pick >= 0 and user_pick <= 2:
    print(images[user_pick])

comp_pick = random.randint(0,2)
print(f"Computer Chose:")
print(images[comp_pick])

if user_pick >= 3 or user_pick < 0:
    print("You picked an invalid number: You lose!")
elif user_pick == 0 and comp_pick == 2:
    print("You Win!")
elif comp_pick > user_pick:
    print("You lose!")
elif comp_pick == user_pick:
    print("It's a draw!")
elif comp_pick == 0 and user_pick == 2:
    print("You lose!")
elif user_pick > comp_pick:
    print("You win!")
