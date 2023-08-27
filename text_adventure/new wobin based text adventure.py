# new wobin based text adventure
import random


import Class_list
import Role_list
import Enemy_list
import Battle


def make_a_character():
    name = input("What's your name?")
    job = Role_list.player_choice()
    R = Role_list
    global player
    player = Class_list.player(name,R.roles[job]["name"],R.roles[job]["attributes"]['maxhp'],R.roles[job]["attributes"]['attack'],R.roles[job]["attributes"]['defence'])


def make_an_enemy():
    e_list = Enemy_list.enemy_data
    keylist = list(Enemy_list.enemy_data)
    enemy_index = random.randrange(0,len(Enemy_list.enemy_data))
    global enemy
    new_e = keylist[enemy_index]
    enemy = Class_list.enemy(e_list[new_e]['name'],e_list[new_e]['hp_max'],e_list[new_e]['atk'],e_list[new_e]['dfp'])


def make_an_item():
    pass


def make_an_event():
    event_list = ['battle','no_event']
    print(f"{player.p_name} is adventuring")
    random_event = random.randrange(0,len(event_list))
    match event_list[random_event]:
        case 'battle':
            make_an_enemy()
            print("Conflict!!!")
            Battle.random_battle(player,enemy)
        case 'no_event':
            print("There's nothing here.")
            input("enter to continue")





def Main():
    print("new adventure")
    make_a_character()
    print(player.p_name)
    print("to adventure!\n\n\n")

    while player.hp_cur > 0:
        make_an_event()
    

Main()