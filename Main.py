from Get_Volume import *

class Fuel_Tank():
    def __init__(self, species):
        self.species = species
        self.safety_margin = 1.5 #-
        self.pressure = 80 # N/mm^2
        self.height = 0 #L in mm
        self.radius = 415 #r_in in mm
        self.thickness = 4 #t in mm
        self.outerradius = self.radius + self.thickness # mm

class Margin_of_safety():
    def __init__(self, name, value):
        self.name = name
        self.value = value


# Global variables
max_height = 891 #L+2r in mm
fuel_mass = 480 #kg


# Start of main loop

volume = get_volume(tank.pressure, fuel_mass)