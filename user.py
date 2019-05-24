#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 01:22:04 2019

@author: seungyeop
"""

import random
import yutnori_map as ym

class User():
    def __init__(self, n_users):
        self.n_user = user_index

        
    def roll(self):
        yut = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        if sum(yut) == 1:
            n_roll = 1
        elif sum(yut) == 2:
            n_roll = 2
        elif sum(yut) == 3:
            n_roll = 3
        elif sum(yut) == 4:
            n_roll = 4
        else:
            n_roll = 5
        return n_roll


if __name__ == __main__:
    """
    example
    total_map = ym.Map()
    user = User(1)
    total_map.select(user.roll(), map_index, user.n_user)
    """