#!/usr/local/bin python
# -*- coding:utf-8 -*-

import random
from XCSRConfig import *
from XCSREnvironment import *
from XCSRClassifier import *
from XCSRClassifierSet import *

class XCSRMatchSet(XCSRClassifierSet):
    def __init__(self,pop,actual_time):
        XCSRClassifierSet.__init__(self,actual_time)
        self.pop = pop
        for cl in self.pop.cls:
            if self.does_match(cl):
                self.cls.append(cl)
        """もし条件部の一致するClassifierで全体の行動部の種類が
        theta_mnaより小さかったらCoveringを実行し,
        env.stateと条件部の一致するClassifierを意図的に生成する.

        Initialize the match set with condition and action from the env's training instance
        """
        while self.num_of_different_actions() < conf.theta_mna:
            cond = []
            clm = XCSRClassifier(cond,actual_time)
            for i in range(len(gb_env.state)):
                if random.random() < conf.p_sharp:
                    cond.append('#')
                else:
                    cond.append(gb_env.state[i])
            clm.condition = cond
            clm.action = gb_env.random_action() # MatchSetのClassifierにない行動部をランダムで返す
            clm.experience = 0
            clm.time_stamp = actual_time
            clm.action_set_size = self.numerosity_sum() + 1
            clm.numerosity = 1
            self.pop.cls.append(clm)
            self.cls.append(clm)
            while self.pop.numerosity_sum() > conf.N:
                cl_del = pop.delete_from_population()
                if cl_del == None:
                    if cl_del in self.cls:
                        self.cls.remove(cl_del)

    def does_match(self,cl):
        """条件部が一致するか"""
        # Env's state is the training instance
        return gb_env.is_condition_matching(cl.condition)

    def num_of_different_actions(self):
        """MatchSet内のClassifierの行動部の種類数を返す"""
        a_list = []
        for cl in self.cls:
            a_list.append(cl.action)
        return len(set(a_list)) # list -> set: removing duplicates

# for debug
# if __name__ == '__main__':
#     env = XCSREnvironment()
#     env.set_state()
#     x = XCSRClassifierSet(env,1)
#     y = XCSRMatchSet(x,env,1)
#     print env.state
#     for cl in y.cls:
#         print cl.condition

