# new wobin based text adventure
import random


import Class_list


def make_a_character():
    name_new = input("What's your name?")
    import Role_list
    job_choice = Role_list.player_choice()
    R = Role_list
    global player
    player = Class_list.player(name_new,R.roles[job_choice]["name"],R.roles[job_choice]["attributes"]['maxhp'])
    

import Enemy_list

def make_an_enemy():
    keylist = Enemy_list.enemy_data.keys()
    new_enemy = random.randrange(0,len(Enemy_list.enemy_data))
    global enemy
    print('keylist')
    print(keylist)
    print('new_enemy')
    print(new_enemy)
    enemy = keylist[new_enemy]
    #enemy = Class_list.enemy(new_enemy['e_name'],new_enemy['hp_max'],new_enemy['atk'],new_enemy['dfp'])
    #print (enemy.e_name)
make_an_enemy()

def make_an_item():
    pass


def make_an_event():
    event_list = ['battle','no_event']
    print(f"{player.p_name} is adventuring")
    random_event = random.randrange(0,len(event_list))
    match event_list[random_event]:
        case 'battle':
            print("Conflict!!!")
            battle()
        case 'no_event':
            print("There's nothing here.")
            input("enter to continue")



def battle():
    make_an_enemy()
    print(f"An {enemy.e_name} appeared")

    input("enter to continue")


def Main():
    print("new adventure")
    make_a_character()
    print(player.p_name)
    print("to adventure!\n\n\n")

    while player.hp_cur > 0:
        make_an_event()
    

Main()