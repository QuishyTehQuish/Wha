a = 10
print(a)


b = ['c','d']

import random
print(random)


class test_class_1:
    var = 345
    def something(self, a1, a2):
        self.var1 = a1
        self.var2 = a2
        self.var3 = self.var


class player:

    def __init__(self,m_name,job_new,hp_max_new,atk,dfp):
        self.p_name = m_name
        self.job = job_new
        self.hp_max = hp_max_new
        self.hp_cur = self.hp_max
        self.atk = atk
        self.dfp = dfp