# 'doc string'
import random
#my version

rps = ["rock","paper","scissor"]

def player_choice(): # function
    print('choose rock paper or scissor')
    p_choice = input()
    if p_choice in rps:
        print("you pick "+str(p_choice))
    else:
        print("try again")
        player_choice()
    c_choice= random.choice(rps)
    print(c_choice)
    if p_choice == c_choice:
        print("tie")
    elif p_choice == "rock" and c_choice == "scissors":
        print("you win")
    elif p_choice == "rock" and c_choice == "paper":
        print("you lose")
    player_choice()


player_choice()
