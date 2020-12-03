# Inputs
p = 8  # [N/mm^2] Pressure inside tank
r = 415.3  # [mm] Radius of tank
t = 3.78  # [mm]  Thickness

# Material Properties
yield_al1 = 276  # [N/mm^2] Aluminum-6061
yield_al2 = 503  # [N/mm^2] Aluminum-7075
yield_steel = 215  # [N/mm^2] AISI Type 304 Stainless Steel
yield_ti = 880  # [N/mm^2] Titanium Ti^-6Al-4V
yield_compositemg = 100  # [N/mm^2] composite Magnesium

yield_list = [yield_al1, yield_al2, yield_compositemg, yield_steel, yield_ti]
MS = []
i = 0
MSi = 0
MSi_min = 0

# Functions
def hoop_stress(p_, r_, t_):
    sigma_hoop = p_ * r_ / t_
    return sigma_hoop


max_stress = hoop_stress(p, r, t)

for i in range(0, len(yield_list)):
    if abs(MSi) < abs(MSi_min):
        MSi = MSi_min
        material_smallest_MS = i
    MSi = abs(yield_list[i] / max_stress - 1)

    MS.append(MSi)

print(" The min MS is ", min(MS), "for material with yield stress", yield_list[i])

def pressure(tank,material):
    sigma_hoop = tank.pressure * tank.radius / tank.thickness
    tank.MS_pressure = material.yield_stress / sigma_hoop - 1
    return tank

