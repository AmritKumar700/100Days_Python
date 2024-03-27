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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#making list of games images in order to print accordingly
games_images = [rock,paper,scissor]
#taking user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#printing games images as per user choice
print(games_images[user_choice])

#generating random number from computer side and printing it
computer_choice = random.randint(0,2)
print("Computer Choice:")
print(games_images[computer_choice])

#Checking if the user enter valid choice
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
#Comparing user and computer choice as per the game rule  
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")










