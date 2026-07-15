import numpy as np
from pathlib import Path
from clawpack.geoclaw import dtopotools

def make_dtopo_from_rsqsim(file,output_dir,fname):
    fault0=dtopotools.Fault()
    fault0.subfaults=[]
    fault0.rupture_type="static"
    J=int(np.floor(file.shape[0]))

    for j in range(J):
        subfault0=dtopotools.SubFault()
        node1=file[j,1:4].tolist()
        node2=file[j,4:7].tolist()
        node3=file[j,7:10].tolist()
        node_list=[node1,node2,node3]

        rake=file[j,10]
        slip=file[j,11]
        subfault0.rise_time=0.5#Massive assumption but let's see where it pays off François
        subfault0.set_corners(node_list,projection_zone="58")#UTM zone for Vanuatu/New Caledonia is 58K
        subfault0.rake=rake
        subfault0.slip=slip
        fault0.subfaults.append(subfault0)
    x,y=fault0.create_dtopo_xy(dx=4/60.)
    dtopo0=fault0.create_dtopography(x,y,slip_tol=1e-3,verbose=50)
    fname=output_dir+"/"+fname+".dtopo"
    dtopo0.write(fname,dtopo_type=1)
    
    return None
def main():
    directory="/Users/seansantellanes/Documents/initial_conditions/Rupture_models/"
    output_dir="/Users/seansantellanes/Documents/initial_conditions/RSQSim_dtopos"
    parent_dir=Path(directory)
    files=sorted([f for f in parent_dir.iterdir() if f.is_file()])
    i=0
    for file in files:
        i+=1
        file_str=str(file)
        filename=file_str.split("/")[-1]
        filename_minus_stem=filename.split(".")[:-1]
        fname=filename_minus_stem[0]+"_"+filename_minus_stem[1]
        if i%100==0:
            data=np.genfromtxt(file,skip_header=1)
            make_dtopo_from_rsqsim(data,output_dir,fname)
main()
