import numpy as np
from pathlib import Path
def compute_ets(eta,dx,dy):
    """
    eta, dx, dy: (eta:np.array,dx:scalar,dy:scalar)

    returns
    -------
    scalar product
    """
    rho=1000#kg/m3
    g=9.8#m/s2
    ets=(rho*g/2)*eta**2*dx*dy #assumes rectangular grid
    ets=np.sum(ets)
    return ets
def main():
    directory="/Users/seansantellanes/Documents/dynamic_topography/dtopos_bicho"#Pyt directory info here
    parent_directory=Path(directory)
    files=[f for f in parent_directory.iterdir() if f.is_file()]
    i=0
    ets_array=np.zeros(len(files))
    for file in sorted(files):
        data=np.genfromtxt(file)
        idx=np.where(data[:,0] != 0)[0]
        filtered_data=data[idx,:]
        dx=data[1,1]-data[0,1]
        dy=dx#assume a square grid
        eta=data[:,3]
        ets_array[i]=compute_ets(eta,dx,dy)
        i+=1
    np.savetxt("/Users/seansantellanes/Documents/Codes/python/energy_analysis/ets_analysis_dtopo_bicho.txt",ets_array,fmt="%.2e")
main()
