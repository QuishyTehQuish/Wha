import random


def damage_formula(target,hp_cur,atk,dfp):
    print(hp_cur)
    print(atk)
    print(dfp)
    damage = (atk - dfp)
    #hp_cur -= damage
    print(f'{target} took {damage} damage!!! and has {hp_cur} remaining')
    return damage

def random_battle(player,enemy):

    while enemy.hp_cur > 0:
        p_action = input('what do you do: 1(attack) 2(skill) 3(item) 4(defend) 5(run)')
        if p_action == '1':
            dam = damage_formula(enemy.name,enemy.hp_cur,player.atk,enemy.dfp)
            print(f'what damagefoumula returned = {dam}')
            enemy.hp_cur -= dam
        elif p_action == '2':
            print('not implemented')
        elif p_action == '3':
            print('also not yet')
        elif p_action == '4':
            print()
        elif p_action == '5':
            runchance = random.randrange(0,3)
            print(f'runchance = {runchance}')
            if runchance == 0:
                print('Your slow...')
            elif runchance >= 1:
                print("you run away")
                break
        
        else:
            print('you fucked up your turn')
