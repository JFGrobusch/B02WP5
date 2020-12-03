# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:16:00 2020

@author: Jan Grobusch
"""

from math import pi, exp

def shellbucklingMS(tank, material):    
    C = ((12/pi**4)*(tank.height**4/(tank.radius**2*tank.thickness**2))*(1-material.poisson**2))
    lam = C**0.5
    k = lam + C*(1/lam)
    Q = (tank.pressure/material.elasticity)*(tank.radius/tank.thickness)**2
    stress = (1.983-0.983*exp(-23.14*Q))*k*(pi**2*material.elasticity/(12*(10-material.poisson**2)))*(tank.thickness/tank.height)**2
    MS = stress/material.yieldstress
    return(MS)