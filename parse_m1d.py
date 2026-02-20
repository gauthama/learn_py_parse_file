# Simplified M1D data file content:
# # Table format: T1D
# # table_unit = null
# # axis1_unit = null
# # axis2_unit = null
# 0.0     3
# 2.3     1.2
# 7.5     0.5
# 1.5     1.0
# 5.0     2
# 0.0     3.4
# 6.9     5.1



#Input:
# 3
# 21    9
# 7     5
# 8     1
# 2
# 0     3
# 6     5

#Output:
# {3: [[21, 7, 8],[9, 5, 1]],
# 2: [[0, 6],[3, 5]]}

def parse_m1d_data_file(file_path):
    result = {}

    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            # Read block size (skip comments/empty lines)
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    tmp_list =line.split()
                    slice_value = tmp_list[0]
                    count = int(float(tmp_list[1]))
                    break
            else:
                break  # EOF reached

            col1 = []
            col2 = []

            for _ in range(count):
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        a, b = map(float, line.split())
                        col1.append(a)
                        col2.append(b)
                        break
                else:
                    raise ValueError("Unexpected EOF inside data block")

            result[slice_value] = [col1, col2]

    #print(result)
    return result

   
# Usage
if __name__ == "__main__":
    file_path = "sample_formats/data/M1D_tiny.data"
    output = parse_m1d_data_file(file_path)
    print(output)