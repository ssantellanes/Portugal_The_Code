#=⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⡤⣤⣄⣤⡴⠶⠟⠛⠉⠉⠁⠀⠀⠀⠀⠉⠉⠛⠷⣦⡀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⡷⣿⣟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀
⠀⠀⠀⢀⣴⠟⠿⣦⣴⠿⠛⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀
⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣤⡀⠀⠀⢀⣀⣀⣠⣤⣤⠶⠟⠋⠀⠀
⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣬⠿⠚⢛⠛⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀⠘⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣄⣀⣀⣀⣤⡶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀
=#

module lasso
export NormArray, CosmicSelector
using LinearAlgebra
function get_norm(x,y)
    #Construct a vector of differences
    z=x.-y #Element-wise differenincing
    return norm(z,2)
end
function NormArray(A,B)
    nr=size(A,1)
    normarray=zeros(nr)
    for i=1:nr
        x=B[1,:,:]
        y=A[i,:,:] #Yes, this could be written better. I do not care.
        normarray[i]=get_norm(x,y)
    end
    return normarray
end
function CosmicSelector(η)
    top_events=zeros(25,2)
    for i=1:25
        info_event=findmin(η)
        top_events[i,1]=info_event[1]
        top_events[i,2]=info_event[2]
        deleteat!(η,info_event[2])
    end
    return top_events
end
end
