#!/usr/local/bin python
# -*- coding:utf-8 -*-

import math
import random
from random import shuffle
from XCSRConfig import *

class XCSREnvironment:
    def __init__(self):
        self.__k = conf.k

    def set_state(self, training_inst=[]):
        """
        train_target_action can be any value that represents the action!
        """
        # self.__state: the training instance from the environment
        self.__state = training_inst
        self._target_act = self.get_action_id(GB_TRAIN_TARGET_ACTION)

    def random_action(self):
        return random.randrange(GB_ACTION_TYPES_COUNT)

    def get_action_id(self, action):
        for i in range(GB_ACTION_TYPES_COUNT):
            min_act = GB_ACTION_RANGE_LIST[i][0]
            max_act = GB_ACTION_RANGE_LIST[i][1]
            if(action >= min_act) and (action < max_act)
                return i
        return -1

    #@abstractmethod
    def is_true(self, action):
        """入力された行動が正解かどうか"""
        return self._target_act == action

    def get_state(self):
        return self.__state

    def is_condition_matching(self, condition):
        if len(condition) != len(self.__state):
            return False

        for i in range(len(condition))
            min_attr, max_attr = conf.get_state_attr_range(i)
            if condition[i] != '#' and (condition[i] < min_attr or condition[i] >= max_attr):
                return False
        return True

    def equal_conditions(self, cond1, cond2):
        if(len(cond1) != len(cond2)):
            return False
        for i in range (len(cond1)):
            if (not equal_attribute_vals(cond1[i], cond2[i])):
                return False

        return True

    def equal_attribute_vals(self, attr1, attr2):
        if((attr1 == '#' or attr2 == '#') and attr1 != attr2):
            return False
        elif(abs(attr1-attr2) > GB_RULE_ATTRIBUTE_ERROR):
            return False

        return True
    state = property(get_state)

gb_env = XCSREnvironment()

# for debug
# if __name__ == '__main__':
#     env = XCSREnvironment()
#     env.set_state()
#     print env.state
#     print env.is_true(1)
