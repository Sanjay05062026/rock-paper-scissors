import random
import time
rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)'''
paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)'''
scissor = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)'''

images = [rock, paper, scissor]
choices = ["rock", "paper", "scissor"]
while True:
    try:
        user_input = int(input("What do you wanna choose???0 for rock, 1 for paper or 2 for scissors\n"))
        user_choice =  int(user_input)
    except ValueError:
        print("Invalid input use numbers between 0-2")
        continue

    if user_choice >=0 and user_choice <=2:
        print(f"Your choice is {choices[user_choice]}")
        print(images[user_choice])

        computer_choice = random.randint(0, 2)
        print("-" * 60)
        print("Computer is thinking...")
        print("-" * 60)
        print(f"Computer choice is {choices[computer_choice]}")
        print(images[computer_choice])
        print("-" * 60)

        if user_choice == computer_choice:
            print("DRAW!")
        elif user_choice == 0 and computer_choice ==2:
            print("You win")
        elif user_choice == 2 and computer_choice == 0:
            print("You Lose")
        elif user_choice>computer_choice:
            print("You win")
        else:
            print("YOU LOSE")
    else:
        print("Enter a VALID NUMBER between 0-2")

    play_again = input("Wanna Play Another Match??? (Y/N)\n").lower()
    if play_again != "y":
        print("Thanks for playing")
        break
