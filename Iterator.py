### Iteration magic###
## Evolving a fuel tank##
import random as rnd

class Fuel_Tank():
    def __init__(self, species):
        self.species = species
        self.safety_factor = 1.5 #-
        self.pressure = 80 # N/mm^2
        self.height = 0 #L in mm
        self.radius = 415 #r_in in mm
        self.thickness = 4 #t in mm
        self.outerradius = self.radius + self.thickness # mm
        # All the safety margins
        self.MS_pressure = 1 #MS_pressure
        self.MS_euler = -1 #MS_euler
        self.MS_shell = 1 #MS_shell
        self.MS_total = self.MS_pressure + self.MS_euler + self.MS_shell
        self.MS = [self.MS_pressure,self.MS_euler,self.MS_shell]

population =[]
def best_finder(number_species, per_species, tanks):
    # Sort by species
    while len(tanks)>0:
        species = []
        for tank in range(per_species):
            species.append(tank.pop())
        population.append(species)
    # Find best from species
    best = []
    best_index = []
    a = 0
    for species in population:
        new = species[0]
        for tank in species:
            old = new
            if new.MS < old.MS:
                best_tank = tank
                best_index_tank = a
            a += 1
        best.append(best_tank)
        best_index.append(best_index_tank)

def natural_selection(tank,ev_speed):
    # check if any margin is not satisfied to fix this first
    safe = True
    for margin in tank.MS:
        if margin < 0:
            safe = False
    # Set positve or negative and find what to change.
    if safe:
        adjuster = 1
        margin = max(tank.MS)
        index_margin = tank. MS.index(max(tank.MS))
    else:
        adjuster = -1
        margin = min(tank.MS)
        index_margin = tank.MS.index(min(tank.MS))
    # Get variables assosiated, currently random
    variables = ['p','r','t','l']
    if index_margin == 0:
        # Variables for pressure: p,r,t1,t2
        variables.pop
        rnd.shuffle(variables)
        change = variables.pop
    elif index_margin == 1:
        # Variables for Euler: p,r,t1,t2,l
        rnd.shuffle(variables)
        change = variables.pop
    elif index_margin == 2:
        # Variables for Shell: p,l,r,t1
        rnd.shuffle(variables)
        change = variables.pop
    else:
        rnd.shuffle(variables)
        change = variables.pop
    # Find the evolution factor
    evolution factor = ev_speed * (x)**(1/2)
    # Change the variable(s)
    if change == 't':
        pass
    elif change == 'r':
        pass
    elif change == 't':
        pass
    elif change == 'l':
        pass

def evolver(tanks):
    # Find best for species
    # Apply normal change
    # copy once
    # multiply and mutate
    # return back to start
    pass

tank = Fuel_Tank(0)
natural_selection(tank)