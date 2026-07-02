import numpy as np
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

out = '/Users/dmelgarm/Kamchatka2025/1952/JASmod7_slab2_interpolated.txt'

fault = np.genfromtxt('/Users/dmelgarm/Slab_models/KamchatkaKuril/kamchatka.fault')
fault_lon = fault[:, 1]
fault_lat = fault[:, 2]

slip1952 = np.genfromtxt('/Users/dmelgarm/Kamchatka2025/1952/JASmod7_slab2.txt')
slip1952_lon = slip1952[:, 1]
slip1952_lat = slip1952[:, 2]
slip1952_slip = slip1952[:, 0]

# Build KDTree for fast nearest neighbor search
slip_coords = np.column_stack((slip1952_lon, slip1952_lat))
tree = cKDTree(slip_coords)

# Query nearest slip point for each fault point
fault_coords = np.column_stack((fault_lon, fault_lat))
distances, indices = tree.query(fault_coords)

# Create fault_slip array with slip values from nearest slip1952 point
fault_slip = slip1952_slip[indices]

plt.scatter(fault_lon, fault_lat, c=fault_slip, cmap='viridis')
plt.colorbar(label='Slip (m)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Fault Slip Distribution')
plt.show()

np.savetxt(out, np.column_stack((fault_slip, fault_lon, fault_lat)), fmt='%.6f %.6f %.6f', header='slip(m) lon lat')

