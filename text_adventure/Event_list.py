import random
import Class_list
import Battle
import Enemy_list



event_list = ['battle','battle','no_event']


def new_event(prog_level,player):
    text = (player.name+" is adventuring")
    print(text)
    random_event = random.randrange(0,len(event_list))
    match event_list[random_event]:
        case 'battle':
            enemy = Class_list.make_an_enemy(Enemy_list)
            print("Conflict!!!")
            reward = Battle.random_battle(player,enemy)
        case 'no_event':
            text = ("There's nothing here.")
            print = text
            #input("enter to continue")
            #reward = 'null'
        case 'treasure':
            text = 'Found treasure'
            reward = {'money':5}


    #print(reward)
    return reward
    
