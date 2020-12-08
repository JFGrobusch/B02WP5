def get_volume(pressure, fuel_mass):
    pressure = 10*pressure #n/mm^2 -> bar
    pressure -= 70
    density = ((6*10**-5)*pressure**3) -(0.0034*pressure**2) +(0.077*pressure) +1.0064 #kg/m^3
    print(density)
    density = density * 1000 # convert to kg/m^3
    volume = fuel_mass / density # m^3
    volume = volume * 10E9
    return volume