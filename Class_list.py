

#Class  skill_template:

cat = 'cat'

class player:

    def __init__(self,m_name,job_new,hp_max_new):
        self.p_name = m_name
        self.job = job_new
        self.hp_max = hp_max_new
        self.hp_cur = self.hp_max

class enemy:

    def __init__(self,e_name,hp_max,atk,dfp):
        self.e_name = e_name
        self.hp_max = hp_max
        self.hp_cur = hp_max
        self.atk = atk
        self.dfp = dfp


n = player('name','jobs','hpmax')
print(n)