from termcolor import colored 
## Import the ascii art from the hands.py file
import hands as ascii
import random

while True:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Type 3 to quit game\n"))
    if choice == 3:
        print("You quit the game!")
        break
    computer_choice = random.randint(0,2)
    ## List of choices
    rock_paper_scissors = ["Rock", "Paper", "Scissors"]
    ## List of ascii art from hands.py
    ascii_art = [ascii.rock, ascii.paper, ascii.scissors]
    print("You chose: " + colored(rock_paper_scissors[choice], "red"))
    print(colored(ascii_art[choice], "red"))

    print("Computer chose: " + colored(rock_paper_scissors[computer_choice], "blue"))
    print(colored(ascii_art[computer_choice], "blue"))

## Compare the choices and output the result
    if choice == computer_choice:
        print("It's a draw!")
    elif choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 1 and computer_choice == 0:
        print("You win!")
    elif choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")

