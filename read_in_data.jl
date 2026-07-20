module read_in_data
export read_in
using NPZ
function read_in(file_path)
    data = npzread(file_path)
    return data
end
end

