import random
rock = """
    _______
---'   ____ )
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image=[rock,paper,scissors]
user_choice=int(input("What do you choice? 0 for rock, 1  for paper and 2 for scissors:\n"))
print(game_image[user_choice])
computer_choice=random.randint(0,2)
print("Computer Choice:")
print(game_image[computer_choice])
if user_choice >=3 or user_choice <0:
    print("your number is invalid.")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice==user_choice:
    print(" It is Draw!")
