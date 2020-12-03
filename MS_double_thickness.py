# Inputs
p = 8  # [N/mm^2] Pressure inside tank
r = 415.3  # [mm] Radius of tank
t1 = 3.78  # [mm]  Thickness of cylindrical wall
t2 = 3.78  # [mm] Thickness of spherical cap

# Material Properties
yield_al1 = 276  # [N/mm^2] Aluminum-6061
yield_al2 = 503  # [N/mm^2] Aluminum-7075
yield_steel = 215  # [N/mm^2] AISI Type 304 Stainless Steel
yield_ti = 880  # [N/mm^2] Titanium Ti^-6Al-4V
yield_compositemg = 100  # [N/mm^2] composite Magnesium

# Cylindrical
yield_list = [yield_al1, yield_al2, yield_compositemg, yield_steel, yield_ti]
MS_cylindrical = []
i = 0
MSi_cylindrical = 0
MSi_min_cylindrical = 0

# Spherical
MS_spherical = []
MSi_spherical = 0
MSi_min_spherical = 0


# Functions
def stress_cylinder(p_, r_, t1_):
    sigma_hoop_cylinder = p_ * r_ / t1_
    sigma_longitudinal_cylinder = p_ * r_ / (2 * t1_)
    max_stress_cylinder_ = max(sigma_hoop_cylinder, sigma_longitudinal_cylinder)

    return max_stress_cylinder_


def stress_sphericalcap(p_, r_, t2_):
    sigma_spherical_ = p_ * r_ / (2 * t2_)

    return sigma_spherical_


max_stress_cylinder = stress_cylinder(p, r, t1)
sigma_spherical = stress_sphericalcap(p, r, t2)

for i in range(0, len(yield_list)):
    if abs(MSi_cylindrical) < abs(MSi_min_cylindrical):
        MSi_cylindrical = MSi_min_cylindrical
        material_smallest_MS_cylindrical = i
    MSi_cylindrical = abs(yield_list[i] / max_stress_cylinder - 1)

    MS_cylindrical.append(MSi_cylindrical)

for i in range(0, len(yield_list)):
    if abs(MSi_spherical) < abs(MSi_min_spherical):
        MSi_spherical = MSi_min_spherical
        material_smallest_MS_spherical = p
    MSi_spherical = abs(yield_list[i] / sigma_spherical - 1)

    MS_spherical.append(MSi_spherical)

print(" The min MS for cylindrical part is ", min(MS_cylindrical), "for material with yield stress", yield_list[i])
print(" The min MS for spherical part is ", min(MS_spherical), "for material with yield stress", yield_list[i])
