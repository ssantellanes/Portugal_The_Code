include("read_in_data.jl")
using .read_in_data
file_path="/Users/seansantellanes/Documents/PORTUGAL_THE_CODE/data/geoclaw_nuevo_totale.npz"
data=read_in(file_path)
println(size(data[:"arr_0"]))
#Remember that arr_0 is the key for most of the things going on in the stitching of things
