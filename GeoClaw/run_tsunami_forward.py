#this script loop into all .dtopo file and make tsunami data
from shutil import copy
import numpy as np
import glob
import os
import subprocess
import gc
from shlex import split
import sys
#main inversion
# dtopo_dir = '/Users/dmelgarm/SandPoint2020/tsunami_inversion/dtopo/'
# setup_path = '/Users/dmelgarm/SandPoint2020/tsunami_inversion/geoclaw/setup/'
# output_path = '/Users/dmelgarm/SandPoint2020/tsunami_inversion/geoclaw/output/'
# sources = np.sort(glob.glob(dtopo_dir+'/gauss*'))

#tide gauge sensitivity
# dtopo_dir = '/Users/dmelgarm/SandPoint2020/tide_gauge_sensitivity/dtopo/'
# setup_path = '/Users/dmelgarm/SandPoint2020/tide_gauge_sensitivity/geoclaw/setup/'
# output_path = '/Users/dmelgarm/SandPoint2020/tide_gauge_sensitivity/geoclaw/output/'
# sources = np.sort(glob.glob(dtopo_dir+'/gauss*'))

dtopo_dir = '/hdd/ssantellanes/powell_sans_mw//'
setup_path = '/home/ssantellanes/Tsunami/Cascadia/geoclaw/setup/'
output_path = '/hdd/ssantellanes/powell_segmented_d/'
sources = np.sort(glob.glob(dtopo_dir+'Segmented-D*'))
sources=sources[50::2]
sources=sources[:41]
print(sources)
number = 0
hot_start=0
for s in sources:
    print(s)
    current_folder=output_path+s.split('/')[-1]
    print(current_folder)
    if os.path.exists(current_folder) == False:
        os.makedirs(current_folder)
    else:
        os.remove(current_folder+'/Makefile')
        os.remove(current_folder+'/setrun.py')
    #Move Make file
    copy(setup_path+'Makefile',current_folder)

    #replace with appropriate dtopo
    current_dtopo=dtopo_dir+s.split('/')[-1]

    IN1 = open(setup_path+'setrun.py').read()
    IN1 = IN1.replace('dtopo_GF',current_dtopo)
    OUT1 = open(current_folder+'/setrun.py','w')
    OUT1.write(IN1)
    OUT1.close()

    #run geoclaw
    os.chdir(current_folder)
    subprocess.call(split('make .output'))
    gc.collect()
    number=number+1
