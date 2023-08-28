import random

#Class  skill_template:

cat = 'cat'

class player_class:

    stats = []
    def __init__(self,m_name,job_new,hp_max_new,atk,dfp,spd):
        self.level = 1
        self.exp = 0
        self.next_level = 1

        self.name = m_name
        self.job = job_new
        self.hp_max = hp_max_new
        self.hp_cur = self.hp_max
        self.atk = atk
        self.dfp = dfp
        self.spd = spd

        self.stats = [self.level,self.exp,self.next_level,self.name,self.job,self.hp_max,self.hp_cur,self.atk,self.dfp,self.spd]
    


def make_a_character(Role_list):
    name = input("What's your name?")
    job = Role_list.player_choice()
    R = Role_list
    player = player_class(name,R.roles[job]["name"],R.roles[job]["attributes"]['maxhp'],R.roles[job]["attributes"]['attack'],R.roles[job]["attributes"]['defence'],R.roles[job]["attributes"]['speed'])
    return player


class enemy_class:

    def __init__(self,e_name,hp_max,atk,dfp,spd):
        self.name = e_name
        self.hp_max = hp_max
        self.hp_cur = hp_max
        self.atk = atk
        self.dfp = dfp
        self.spd = spd


def make_an_enemy(Enemy_list):
    e_list = Enemy_list.enemy_data
    keylist = list(Enemy_list.enemy_data)
    enemy_index = random.randrange(0,len(Enemy_list.enemy_data))
    global enemy
    new_e = keylist[enemy_index]
    enemy = enemy_class(e_list[new_e]['name'],e_list[new_e]['hp_max'],e_list[new_e]['atk'],e_list[new_e]['dfp'],e_list[new_e]['dfp'])
    return enemy