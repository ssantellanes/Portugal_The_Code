#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:39:46 2021

@author: dmelgarm
"""
from numpy import genfromtxt,where,savetxt
import sys
sys.path.append('/Users/seansantellanes/gmsh')
import gmsh_tools
from matplotlib import pyplot as plt



mshout = '/Users/seansantellanes/Downloads/vanuatu.mshout' #outout file
mshin = '/Users/seansantellanes/Downloads/vanuatu.msh'  #what you made with gmsh
mudpy_fault='/Users/seansantellanes/Downloads/vanuatu.fault'

gmsh_tools.gmsh2ascii(mshout,mshin,utm_zone='58',flip_lon=True,flip_strike=True)
mesh=genfromtxt(mshout)

i=where(mesh[:,-2]>360)[0]
mesh[i,-2] -=360
i=where(mesh[:,-2]<180)[0]
mesh[i,-2] += 90
i=where(mesh[:,-2]<189)[0]
mesh[i,-2] += 60
i=where(mesh[:,-2]<209)[0]
mesh[i,-2] += 40


h=' fault No. , centroid(lon,lat,z[km]) , node2(lon,lat,z[km]) , node3(lon,lat,z[km]) , mean vertex length(km) , area(km^2) , strike(deg) , dip(deg)'
savetxt(mshout,mesh,fmt='%d\t'+12*'%.6f\t'+4*'%.2f\t',header=h)

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
