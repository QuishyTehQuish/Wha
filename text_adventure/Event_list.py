import random
import Class_list
import Battle
import Enemy_list





def new_event(prog_level,player):
    event_list = ['battle','no_event']
    print(f"{player.name} is adventuring")
    random_event = random.randrange(0,len(event_list))
    match event_list[random_event]:
        case 'battle':
            enemy = Class_list.make_an_enemy(Enemy_list)
            print("Conflict!!!")
            Battle.random_battle(player,enemy)
        case 'no_event':
            print("There's nothing here.")
            input("enter to continue")