#!/usr/local/bin python
# -*- coding:utf-8 -*-

# Range of hand synergy ranges
GB_RULE_ATTRIBUTES = [[0,1],
                      [1,2],
                      [2,3]]
GB_RULE_ATTRIBUTES_COUNT = len(GB_RULE_ATTRIBUTES)

# Threshold to differentiate from two attribute values
GB_RULE_ATTRIBUTE_ERROR = 0.001

# Action is some specific concerned element's value which is given from observing some object
# Here, it could be the tilting action, specified by tilting angle of the plate being balanced on the hand
GB_ACTION_RANGE_LIST =[] #Eg: [0.0, 1.0], [1.0, 2.0], ..., [9.0-10.0]
GB_ACTION_TYPES_COUNT = len(GB_ACTION_RANGE_LIST)

# Targeted action value as the goal for the training.
GB_TRAIN_TARGET_ACTION = 0.0

class XCSRConfig:
    k = 2
    N = 600
    max_iterations = 3000
    max_experiments = 10

    alpha = 0.1
    beta = 0.2
    gamma = 0.71
    delta = 0.1
    myu = 0.04
    nyu = 5
    chi = 0.8

    epsilon_0 = 10

    theta_ga = 25
    theta_del = 20
    theta_sub = 20
    theta_mna = GB_ACTION_TYPES_COUNT

    p_sharp = 0.33
    p_explr = 1.0

    doGASubsumption = True
    doActionSetSubsumtion = True

    def get_state_attr_range(self, i):
        if i < 0 or i >= len(GB_RULE_ATTRIBUTES_COUNT):
            return 0,0
        return GB_RULE_ATTRIBUTES[i][0], GB_RULE_ATTRIBUTES[i][1]

XCSRConfig = XCSRConfig()
conf = XCSRConfig
