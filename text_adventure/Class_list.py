import random

# python fuckin sucks
def clamp(n,min,max):
    if min < n < max:
        return n
    elif n <= min:
        return min
    elif n >= max:
        return max


class player_class:

    stats = []
    def __init__(self,m_name:str,job_new:str,hp_max_new:int,atk:int,dfp:int,spd:int):
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
    

    
def level_up(player:object):
    player.level += 1
    player.exp = clamp(player.next_level - player.exp,0,player.next_level)
    player.next_level = int(player.next_level * 2)
    text = ('Your now level '+str(player.level))
    print(text)
    #will change
    choice = input('1:increase 3 random stats, 2:pick 2 stats, 3:gain ability')
    c = ['1','2','3']
    playerstats = [player.hp_max,player.atk,player.dfp,player.spd]
    new_stat = 0
    if choice in c:
        match choice:
            case '1': #broken
                for i in range(3):
                    new_stat = random.choice(playerstats)
                    new_stat += 1
                    print(new_stat)
            case '2':
                for i in range(2):
                    e = input('pick stat... 1:Max hp, 2:Atk, 3:Dfp, 4:Spd')
                    match e:
                        case '1':
                            player.hp_max += 1
                        case '2':
                            player.atk += 1
                        case '3':
                            player.dfp += 1
                        case '4':
                            player.spd += 1
            case '3':
                pass
    else:
        print("get nothing")
    print(player.stats)
    return player





def make_a_character(Role_list):
    name = input("What's your name?")
    job = Role_list.player_choice()
    R = Role_list
    player = player_class(name,R.roles[job]["name"],R.roles[job]["attributes"]['maxhp'],R.roles[job]["attributes"]['attack'],R.roles[job]["attributes"]['defence'],R.roles[job]["attributes"]['speed'])
    return player


class enemy_class:

    def __init__(self,e_name:str,hp_max:int,atk:int,dfp:int,spd:int,base_exp:int):
        self.name = e_name
        self.hp_max = hp_max
        self.hp_cur = hp_max
        self.atk = atk
        self.dfp = dfp
        self.spd = spd

        self.exp = base_exp


def make_an_enemy(Enemy_list):
    e_list = Enemy_list.enemy_data
    keylist = list(Enemy_list.enemy_data)
    enemy_index = random.randrange(0,len(Enemy_list.enemy_data))
    global enemy
    new_e = keylist[enemy_index]
    enemy = enemy_class(e_list[new_e]['name'],e_list[new_e]['hp_max'],
                        e_list[new_e]['atk'],e_list[new_e]['dfp'],e_list[new_e]['spd'],
                        e_list[new_e]['base_exp'])
    return enemy