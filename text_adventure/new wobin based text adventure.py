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
player_money = int(0)
    





def make_an_item():
    pass


def event_manager():
    choices = ["1",'2','3','4']
    choice = input("What will you do? 1:Adventure, 2:Manage inventory, 3:Status, 4:die")
    if choice in choices:
        match choice:
            case '1':
                event = Event_list.new_event(progression,player)
                #print(event)
                #print(type(event))
                if isinstance(event,dict):
                    print('here')
                    for i in event:
                        if 'items' in event[i]:
                            print('ite')
                            gain_items = event[i]['items']
                            for i in gain_items:
                                print('yoa')
                                global player_inventory
                                player_inventory.append(i)
                            print(f'You gained {gain_items}')
                        elif 'money' in event[i]:
                            gain_money = event[i]['money']
                            global player_money 
                            player_money += gain_money
                            print(f'You gained {gain_money}')

            case '2':
                print(f"Your inventory\n{player_inventory}\nYour money: {player_money}")
            case '3':
                print(player.stats)
                
            case '4':
                print('leathal damage')
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