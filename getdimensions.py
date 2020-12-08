#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:22:01 2020



Import into main document via :
    
        import getradius from getdimensions

@author: jangrobusch
"""

from math import pi
import numpy as np

def volume(r, maxheight):
    V = pi*r*(maxheight*r-(2/3)*r**2)
    return(V)


def getdimensions(tank, targetvolume, maxheight):
    stepsize = 0.1
    h = maxheight
    Vdiffs = []
    rlist = []
    for i in np.arange(0, 0.5*h, stepsize):
        rlist.append(i)
        Vdiffs.append(abs(volume(i, h)-targetvolume))   
    tank.radius = rlist[Vdiffs.index(min(Vdiffs))]
    tank.height = h - 2*tank.radius
    


class tanky:
    def __init__(self,):
        self.radius = 0.
        self.height = 0.

"""
maxheight = 1.7E3
V = 3E8

tank = tanky()
tank = getdimensions(tank, V, maxheight)
print(tank.radius, tank.height)
"""

    
    
    


        