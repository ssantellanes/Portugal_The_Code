#=
#Common params used in the llw2d and tdac codes
#
=#

module m_params
    STDERR::Int64=0
    STDOUT::Int64=6
    g0::Float64=9.80665
    
    nx::Int64=400
    ny::Int64=400
    no::Int64=49
    dx::Float64=1000.0
    dy::Float64=1000.0
    dt::Float64=1.0
end
