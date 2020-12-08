from Get_Volume import *
from getdimensions import *
#from MS_single_thickness import *
from MS_shell_buckling import *

class Fuel_Tank():
    def __init__(self, species):
        self.species = species
        self.safety_factor = 1.5 #-
        self.pressure = 80 # N/mm^2
        self.height = 0 #L in mm
        self.radius = 415 #r_in in mm
        self.thickness = 4 #t in mm
        self.outerradius = self.radius + self.thickness # mm
        self.fuel_mass = 480 #kg
        self.volume = get_volume(self.pressure, self.fuel_mass)
        # All the safety margins
        self.MS_pressure = -1
        self.MS_euler = 0
        self.MS_shell = 0
        self.MS_total = self.MS_pressure + self.MS_euler + self.MS_shell
        self.MS = [self.MS_pressure,self.MS_euler,self.MS_shell]
    
    def safety_check(self):
        self.MS = [self.MS_pressure,self.MS_euler,self.MS_shell]
        for margin in self.MS:
            if margin < 0:
                self.safety = False
                break
            else:
                self.safety = True

class Margin_of_safety():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Material():
    def __init__(self, name, yield_strength, poisson, elasticity):
        self.name = name
        self.yield_strength = yield_strength
        self.poisson = poisson
        self.elasticity = elasticity

"""
# Global variables
max_height = 891 #L+2r in mm
fuel_mass = 480 #kg

number_species = 20
total_tanks = 100
per_species = total_tanks / number_species
total_generations = 10
ev_speed = 0.5

# Start of main loop

volume = get_volume(tank.pressure, fuel_mass)
"""

def pressure(tank,material):
    sigma_hoop = (tank.pressure/10) * tank.radius / tank.thickness
    tank.MS_pressure = material.yield_strength / sigma_hoop - 1

safety_factor = 1.25

#material = Material('Alu', 276/safety_factor, 0.33, 68.9E3)
material = Material('tit', 880/safety_factor, 0.342, 113.8E3)

tank = Fuel_Tank(0)
getdimensions(tank, tank.volume, 891)
tank.thickness = 0.1
tank.safety_check()
while not tank.safety:
    #print(tank.thickness)
    #print(tank.MS)
    tank.thickness += 0.1
    pressure(tank,material)
    shellbucklingMS(tank,material)
    tank.safety_check()
    print(tank.MS)
print(tank.thickness)
print(tank.height)
print(tank.radius)
