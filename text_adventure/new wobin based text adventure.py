# new wobin based text adventure
import random


import Class_list
import Role_list
import ability_list
import Event_list


# python fuckin sucks
def clamp(n,min,max):
    if min < n < max:
        return n
    elif n <= min:
        return min
    elif n >= max:
        return max

#list stored in objects so they can be init once and called repeatidly
#items 
#abilities

# game variables
player = 0
progression = 0
player_inventory = []    
player_money = int(0)
    


def _player_status_update():
    player.stats = [player.level,player.exp,player.next_level,player.name,player.job,player.hp_max,player.hp_cur,player.atk,player.dfp,player.spd]


def make_an_item():
    pass


def event_manager():
    global player
    choices = ["1",'2','3','4']
    choice = input("What will you do? 1:Adventure, 2:Manage inventory, 3:Status, 4:die")
    if choice in choices:
        match choice:
            case '1':
                event = Event_list.new_event(progression, player)
                #print(event)
                #print(type(event))
                if isinstance(event,dict):
                    for i in event:
                        if 'items' in event[i]:
                            gain_items = event[i]['items']
                            for i in gain_items:
                                global player_inventory
                                player_inventory.append(i)
                            print(f'You gained {gain_items}')
                        elif 'money' in event[i]:
                            gain_money = event[i]['money']
                            global player_money 
                            player_money += gain_money
                            text = ("you gained"+str(gain_money)+'money')
                            print(f'You gained {gain_money} money')
                        elif 'exp' in event[i]:
                            gain_exp = event[i]['exp']                            
                            player.exp += gain_exp
                            print(f'You gained {gain_exp} exp')
                            if player.exp >= player.next_level:
                                #global player
                                player = Class_list.level_up(player)



            case '2':
                print(f"Your inventory\n{player_inventory}\nYour money: {player_money}")
            case '3':
                _player_status_update()
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