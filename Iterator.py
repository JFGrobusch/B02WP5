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
        self.MS_pressure = 4 #MS_pressure
        self.MS_euler = 5 #MS_euler
        self.MS_shell = 4 #MS_shell
        self.MS_total = self.MS_pressure + self.MS_euler + self.MS_shell
        self.MS = [self.MS_pressure,self.MS_euler,self.MS_shell]

population =[]

number_species = 20
total_tanks = 100
per_species = total_tanks / number_species
total_generations = 10
ev_speed = 0.1

def natural_selection(tanks):
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

def evolver(tank,ev_speed):
    # check if any margin is not satisfied to fix this first
    safe = True
    for margin in tank.MS:
        if margin < 0:
            safe = False
    print(safe)
    # Set positve or negative and find what to change.
    if safe:
        adjuster = -1
        margin = max(tank.MS)
        index_margin = tank. MS.index(max(tank.MS))
    else:
        adjuster = 1
        margin = min(tank.MS)
        index_margin = tank.MS.index(min(tank.MS))
    print(margin, index_margin)
    # Get variables assosiated, currently random
    if index_margin == 0:
        # Variables for pressure: p,r,t1,t2
        variables = ['p','r','t']
        rnd.shuffle(variables)
        change = variables[0]
    elif index_margin == 1:
        # Variables for Euler: p,r,t1,t2,l
        variables = ['p','r','t','l']
        rnd.shuffle(variables)
        change = variables[0]
    elif index_margin == 2:
        # Variables for Shell: p,l,r,t1
        variables = ['p','r','t','l']
        rnd.shuffle(variables)
        change = variables[0]
    else:
        variables = ['p','r','t','l']
        rnd.shuffle(variables)
        change = variables[0]
    print(change)
    # Find the evolution factor
    ev_factor = ev_speed * (abs(margin))**(1/2)
    print(ev_factor)
    # Change the variable(s)
    if change == 'p':
        tank.pressure += adjuster * ev_factor
    elif change == 'r':
        tank.radius += adjuster * ev_factor
    elif change == 't':
        tank.thickness += adjuster * ev_factor
    elif change == 'l':
        tank.height += adjuster * ev_factor
    evolved_tank = [tank,ev_factor]
    return evolved_tank

def multiply(tanks,evolved_tank):
    tank = evolved_tank[0]
    ev_factor = evolved_tank[1]
    print(tank,ev_factor)
    tanks.append(tank)
    # Mutate them
    for tank in range(int(per_species-1)):
        variables = ['p','r','t','l']
        rnd.shuffle(variables)
        change = variables[0]
        if change == 'p':
            tank.pressure += adjuster * ev_factor
        elif change == 'r':
            tank.radius += adjuster * ev_factor
        elif change == 't':
            tank.thickness += adjuster * ev_factor
        elif change == 'l':
            tank.height += adjuster * ev_factor
        tanks.append(tank)
    return tanks


tanks = []
tank = Fuel_Tank(0)
evolved_tank = evolver(tank,0.5)
tank = evolved_tank[0]
print(tank.pressure,tank.radius,tank.thickness,tank.height)
tanks.append(multiply(tanks,evolved_tank))
print(tanks)
# main loop

#start with tanks
#Find best tanks
#Evolve best tanks
#evolved.append(evolver)
#put in evolved[]
#Empty tanks
#Multiply
#append to new tanks