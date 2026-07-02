from numpy import genfromtxt,where,float64,r_,expand_dims
from glob import glob
import sys

sys.path.append('/Users/seansantellanes/gmsh')
from gmsh_tools import xyz2gmsh
from matplotlib.path import Path

#Gmsh output file name
gmsh_out='/Users/seansantellanes/Downloads/vanuatu.gmsh'
macinnes_path = genfromtxt('/Users/seansantellanes/Documents/Vanuatu/kml/maccinnnes_path.txt')

#Contours files 
contour_files= glob('/Users/seansantellanes/Downloads/van_test_contours.txt')


#Parse contours file
contours=genfromtxt('/Users/seansantellanes/Documents/Vanuatu/kml/hires_trench.xy')
#fix depth
contours[:,2]/=1000

ks=0
for k in range(len(contour_files)):
    f=open(contour_files[k])
    while True:
        line=f.readline().rstrip()
        if not line: #Exit loop
            break
        #Assign line info to array
        if '>' not in line: #It's not a segment header
            if ks==0:
#                contours=expand_dims(float64(line.split('\t')),0)
                r_[contours,expand_dims(float64(line.split('\t')),0)]   
                ks+=1
            else:
                contours=r_[contours,expand_dims(float64(line.split('\t')),0)]   
               
    f.close()

#Now filter things
# Create a Path object from macinnes_path
macinnes_poly = Path(macinnes_path[:, :2])

# Find which contour points are inside the path
inside = macinnes_poly.contains_points(contours[:, :2])

# Keep only the points inside the path
contours = contours[inside]

print(contours[-1,:])



#Write gmsh file
xyz2gmsh(gmsh_out,contours[:,0],contours[:,1],contours[:,2],coord_type='UTM',projection_zone='58')


    
