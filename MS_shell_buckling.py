# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:16:00 2020

@author: Jan Grobusch
"""

from math import pi, exp
from mmToSI import toSI, tomm

def shellbucklingMS(tank, material):
    tank = toSI(tank)    
    C = ((12/pi**4)*(tank.height**4/(tank.radius**2*tank.thickness**2))*(1-material.poisson**2))
    lam = C**0.5
    k = lam + C*(1/lam)
    Q = (tank.pressure/material.elasticity)*(tank.radius/tank.thickness)**2
    criticalstress = (1.983-0.983*exp(-23.14*Q))*k*(pi**2*material.elasticity/(12*(10-material.poisson**2)))*(tank.thickness/tank.height)**2
    bucklingstress = material.yield_strength*(tank.MS_pressure+1)
    tank.MS_shell = bucklingstress/criticalstress
    tank = tomm(tank)
    return(tank)