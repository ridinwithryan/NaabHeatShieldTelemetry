import numpy as np

# Casimir Force Simulation
h = 6.626e-34  # Planck's constant (J·s)
c = 3e8        # Speed of light (m/s)
A = 0.0001     # Plate area (1 cm², m²)
d = np.linspace(1e-6, 5e-6, 100)  # Separation (1-5 microns, m)

# Casimir force (N) per unit area
force = -((np.pi**2 * h * c * A) / (240 * d**4)) / A
energy_density = 10**113  # Theoretical ZPE (J/m³)

print(f"Max Force: {min(force):.2e} N/m² at 1 micron")
print(f"ZPE Influence: {energy_density:.2e} J/m³ shapes vacuum pull")
