# wobin based text adventure
import os


class play:
    name = "new play"


import Class_list

#from Class import player_choice


quit()



# start game, sets var
import random
print ('wobin adventure v.0.1')
print ('what is your name')
input()
print ('your name is wobin')
print ('these are your stats')
maxhp = 100
hp = 100
attack = 10
defence = 10
speed = 5
print('hp= '+str(hp))
print('atk= '+str(attack))
print('def= '+str(defence))
print('spd= '+str(speed))
print()

ename = ''
emaxhp = 1
ehp =1
eattack = 1
edefence = 1
espeed = 1






#enemy code
def enemy():
    # slime
    ename = 'slime'
    emaxhp = 30 #big slime
    ehp = 30
    eattack = 5
    edefence = 5
    espeed = 5
    

#combat script
def battle():
    enemy()
    global hp
    print('wobin ran into '+ename)
    combat = True
    while combat == True:
        print('1 attack')
        print('2 defend')
        print('3 spell')
        print('4 run away')
        print('5 status')
        action = input()
        if action == '1':
            print('wobin swung wildly')
            hp = hp-10
            print()
        elif action == '2':
            print('wobin curled up')
            print()
        elif action == '3':
            print('wobin cant spell')
            print()
        elif action == '4':
            combat = False
            print('wobin left')
            print()
        elif action == '5':
            print('status')
            print('hp= '+str(hp)+'/'+str(maxhp))
            print('atk= '+str(attack))
            print('def= '+str(defence))
            print('spd= '+str(speed))
            print()
        else:
            continue
            print()
        
    print('wobin gained nothing')
    hp = maxhp
    print ('hp restored '+str(hp)+'/'+str(maxhp))
    input()


print('1 for battle')
b = input()
if b == '1':
    battle()

