using Plots
using DelimitedFiles
using StatsBase
data_fakequakes=readdlm("/Users/seansantellanes/Documents/Codes/python/energy_analysis/ets_analysis_dtopo_bicho.txt")
b=10.0.^(-2:8)
histogram(data_fakequakes,bins=b,xscale=:log10,xlim=extrema(data_fakequakes),label="FakeQuakes",
          xlabel="Ets [erg]",ylabel="Count",legend=:outertopright)
data_rsqsim=readdlm("/Users/seansantellanes/Documents/Codes/python/energy_analysis/ets_analysis_dtopo_rsqsim.txt")
mode_fakequakes=median(data_fakequakes)
mode_rsqsim=median(data_rsqsim)
histogram!(data_rsqsim,bins=b,xscale=:log10,alpha=0.5,label="RSQSim")
vline!([1.34e+01],color=:black,label="2023 M7.0")
vline!([mode_fakequakes],color=:blue,label="FakeQuakes Median ETS",line=:dot,linewidth=3)
vline!([mode_rsqsim],color=:red,label="RSQSim Median ETS",line=:dot,linewidth=3)
savefig("/Users/seansantellanes/Documents/Codes/julia/COSMIC/histogram.png")
