import random


def damage_formula(target:object,hp_cur:int,atk:int,dfp:int):
    damage = (atk - dfp)
    #hp_cur -= damage
    print(f'{target} took {damage} damage!!! and has {hp_cur-damage} remaining')
    return damage


def turn_order(p_speed:int,p_atb:int,e_speed:int,e_atb:int):
    print(f"psped = {p_atb}, esped = {e_atb}")
    ps = p_atb + p_speed
    es = e_atb + e_speed
    return [ps,es]

    
def random_battle(player:object,enemy:object):
    print(f"A {enemy.name} appeared")
    turnspeed = [player.spd,enemy.spd]

    while enemy.hp_cur > 0 and player.hp_cur > 0:
        turnspeed = turn_order(player.spd,turnspeed[0],enemy.spd,turnspeed[1])

        if turnspeed[0] > turnspeed[1]:
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
            
            turnspeed[0] = 0

        elif turnspeed[1] > turnspeed[0]:
            #change to enemy action list
            print(f"{enemy.name} Attacks")
            dam = damage_formula(player.name,player.hp_cur,enemy.atk,player.dfp)
            player.hp_cur -= dam
            #print(f"You took {dam}")

            turnspeed[1] = 0
    

    exp = {'exp' : enemy.exp}
    items = {'items' : ["item placeholder", "item placeholder"]}
    money = {'money' : random.randrange(0,3)}
    reward = {1:items,2:money,3:exp}
    print (reward)
    return reward