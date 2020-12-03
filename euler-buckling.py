import math

# Inputs
r = 415.3  # [mm] Radius of Cross-section
L = 891  # [mm] Length of cylindrical Part
t1 = 3.78  # [mm] minimum thickness of cross-section

# Material Properties
yield_al1 = 276  # [N/mm^2] Aluminum-6061
yield_al2 = 503  # [N/mm^2] Aluminum-7075
yield_steel = 215  # [N/mm^2] AISI Type 304 Stainless Steel
yield_ti = 880  # [N/mm^2] Titanium Ti^-6Al-4V
yield_compositemg = 100  # [N/mm^2] composite Magnesium

E_al1 = 68900  # [N/mm^2] Aluminum-6061
E_al2 = 71700  # [N/mm^2]Aluminum-7075
E_steel = 193000  # [N/mm^2]   AISI Type 304 Stainless Steel
E_ti = 113800  # [N/mm^2]  Titanium Ti^-6Al-4V
E_carbonfibre = 530000  # [N/mm^2]  Carbon fibre7

difference = []

yield_list = [yield_al1, yield_al2, yield_compositemg, yield_steel, yield_ti]
E_list = [E_al1, E_al2, E_steel, E_ti, E_carbonfibre]

# Section Properties
A = 2 * math.pi * r * t1
I = math.pi * (r ** 3) * t1

# Euler Buckling Check
sigma_critical_euler = []
for i in range(0, len(yield_list)):
    sigma_critical_euleri = (math.pi ** 2) * E_list[i] * I / (A * (L ** 2))
    if sigma_critical_euleri > yield_list[i]:
        sigma_critical_euler.append(sigma_critical_euleri)
        print("Success: The material yields before buckling", "with critical buckling stress", sigma_critical_euleri,
              "for material", yield_list[i])

        differencei = sigma_critical_euleri - yield_list[i]
        difference.append(differencei)



    else:
        sigma_critical_euler.append(1)
        print("Failure: The material buckles before yielding", "with critical buckling stress", sigma_critical_euleri,
              "for material", yield_list[i])

print(difference)
print("The best difference is", max(difference))
