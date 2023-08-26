import random
options= ["rock", "paper", "scissors"]

def get_choices():
    player_choice = input("Enter a choice: ")
    computer_choice= random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock" and computer == "scissors":
        return "rock smashes scissors! You win!"
    elif player == "rock" and computer == "paper":
        return  "You lose!"

#check_win("Rock", "paper")










#my version

rps = ["rock","paper","scissor"]

def p():
    print('choose rock paper or scissor')
    p_choice = input()
    if p_choice in rps:
        print("you pick "+str(p_choice))
    else:
        print("try again")
        p()
    c_choice= random.choice(rps)
    print(c_choice)
    if p_choice == c_choice:
        print("tie")
    elif p_choice == "rock" and c_choice == "scissors":
        print("you win")
    elif p_choice == "rock" and c_choice == "paper":
        print("you lose")
    p()