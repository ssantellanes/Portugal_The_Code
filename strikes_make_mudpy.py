from numpy import genfromtxt,where,savetxt
import sys
sys.path.append('/Users/seansantellanes/gmsh')
import gmsh_tools
from matplotlib import pyplot as plt
mshout = '/Users/seansantellanes/Downloads/vanuatu_fine.mshout.txt'
mudpy_fault='/Users/seansantellanes/Downloads/vanuatu.fault'
gmsh_tools.make_mudpy_fault(mshout,mudpy_fault)

f=genfromtxt(mudpy_fault)

plt.figure()
plt.scatter(f[:,1],f[:,2],c=f[:,4],cmap='jet')
plt.colorbar(label='strike')
plt.show()

plt.figure()
plt.scatter(f[:,1],f[:,2],c=f[:,5],cmap='jet')
plt.colorbar(label='dip')
plt.show()
