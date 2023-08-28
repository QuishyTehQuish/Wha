# new wobin based text adventure
import random


import Class_list
import Role_list
import spells_list
import Event_list


#list stored in objects so they can be init once and called repeatidly
#items 
#abilities

# game variables
progression = 0
player_inventory = []    
player_money = 0
    





def make_an_item():
    pass


def event_manager():
    choices = ["1",'2','3']
    choice = input("What will you do? 1:Adventure, 2:Manage inventory, 3:kill yourself")
    if choice in choices:
        match choice:
            case '1':
                Event_list.new_event(progression,player)
            case '2':
                print(f"Your inventory\n{player_inventory}\nYour money: {player_money}")
            case '3':
                player.hp_cur =  0





def Main():
    print("new adventure")
    global player
    player = Class_list.make_a_character(Role_list)
    print(player.name)
    print("to adventure!\n\n\n")

    while player.hp_cur > 0:
        event_manager()
    print("You died")
    restart = input("restart? y/n")
    if restart == "y":
        Main()
    

Main()