#=
*    .  *       .             *
                         *
 *   .        *       .       .       *
   .     *
           .     .  *        *
       .                .        .
.  *           *                     *
                             .
         *          .   *
------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/art/2536

COseismic slip Statistic MIxing Codes (COSMIC)
An implementation of Joseph Chan's (The Ohio State University) Bi-Gaussian Ensemble Kalman Filter (BGEnKF)
for use in tsunami modelling.
=#
include("read_in_data.jl")
include("lasso.jl")

using .read_in_data
using .lasso
file_path="/Users/seansantellanes/Documents/PORTUGAL_THE_CODE/data/geoclaw_nuevo_totale.npz"
data=read_in(file_path)
#println(size(data[:"arr_0"]))
#Remember that arr_0 is the key for most of the things going on in the stitching of things
#But like also remember that it's eta for the real_event.npz
real_data_file_path="/Users/seansantellanes/Documents/PORTUGAL_THE_CODE/data/real_event.npz"
real_data=read_in(real_data_file_path)
η=NormArray(data[:"arr_0"],real_data[:"eta"])
top_events=CosmicSelector(η)
println(top_events)
