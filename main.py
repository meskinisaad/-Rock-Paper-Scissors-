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
choices = [rock, paper, scissors]

ur_choice = int(input("What do you choose? 0-rock, 1-paper or 2-scissors: "))
#if i choose 0-rock
if ur_choice == 0:
    print("ur choice:")
    print(rock)
    computer_choice = random.choice(choices)
    print("computer choice:")
    print(computer_choice)
    if computer_choice == rock:
        print("draw")
    elif computer_choice == paper:
        print("you lose")
    elif computer_choice == scissors:
        print("you win")
    else:
        print("error")
# if i choose 1-paper
if ur_choice == 1:
    print("ur choice:")
    print(paper)
    computer_choice = random.choice(choices)
    print("computer choice:")
    print(computer_choice)
    if computer_choice == rock:
        print("you win")
    elif computer_choice == paper:
        print("draw")
    elif computer_choice == scissors:
        print("you lose")
    else:
        print("error")
# if i choose 1-paper
if ur_choice == 2:
    print("ur choice:")
    print(scissors)
    computer_choice = random.choice(choices)
    print("computer choice:")
    print(computer_choice)
    if computer_choice == rock:
        print("you lose")
    elif computer_choice == paper:
        print("you win")
    elif computer_choice == scissors:
        print("draw")
    else:
        print("error")


