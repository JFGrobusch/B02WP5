# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:20:15 2020

@author: Jan Grobusch
"""


def toSI(tank):
    tank.pressure = tank.pressure/(1000**2) # N/m^2
    tank.height = tank.height*1000 #L in m
    tank.radius = tank.radius*1000 #r_in in m
    tank.thickness = tank.thickness*1000 #t in m    
    return(tank)


def tomm(tank):
    tank.pressure = tank.pressure*(1000**2) # N/mm^2
    tank.height = tank.height/1000 #L in mm
    tank.radius = tank.radius/1000 #r_in in mm
    tank.thickness = tank.thickness/1000 #t in mm    
    return(tank)

def toSIm(material):
    material.yield_strength = material.yield_strength*(1000**2)
    material.elasticity = material.elasticity*(1000**2)
    return(material)

def tommm(material):
    material.yield_strength = material.yield_strength/(1000**2)
    material.elasticity = material.elasticity/(1000**2)
    return(material)