def get_volume(pressure, fuel_mass):
    pressure -= 70
    density = ((6*10**-5)*pressure**3) -(0.0034*pressure**2) +(0.077*pressure) +1.0064 #kg/L
    density = density * 1000 # convert to kg/m^3
    volume = fuel_mass / density # m^3
    volume = volume * 1E9
    print(f'Fuel density{density}, tank volume{volume}')
    return volume