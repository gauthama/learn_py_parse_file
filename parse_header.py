
# Sample header content:
    # Table format: 2D
    # table_unit = Ohm
    # axis1_unit = degC
    # axis2_unit = %

#from learn_py_parse_file.parse_data_file import extract_dim_from_header
from parse_data_file import extract_dim_from_header
import re

# def extract_units_using_regular_expressions(file_path):
#     #import re

#     units = {}

#     pattern = re.compile(r"#\s*axis(\d+)_unit\s*=\s*(.+)")

#     with open("data.txt") as f:
#         for line in f:
#             m = pattern.match(line)
#             if m:
#                 units[m.group(1)] = m.group(2)

def get_dimension_from_data_file(file_path):
    first_line = open(file_path, "r", encoding="utf-8").readline().rstrip("\n")
    prefix = "# Table format: "
    suffix = "D"
    dimension = extract_dim_from_header(first_line, prefix, suffix)
    return dimension

# Input: {'1': 'degC', '2': '%', '3': 'Nm'}
# Output: {'D1': 'Nm', 'D2': '%', 'D3': 'degC'}
def reverse_dimension_units(units_dict):
    # sort keys numerically
    keys = sorted(units_dict.keys(), key=int)

    # reverse values according to numeric key order
    reversed_values = [units_dict[k] for k in keys[::-1]]

    # build result dictionary
    result = {}
    for index, value in enumerate(keys):
        result[f"D{value}"] = reversed_values[index]

    #print(result)
    return result

def parse_header_of_data_file(file_path):
    table_unit = None

    dimension = get_dimension_from_data_file(file_path)
    #print(f"dimension: {dimension}")
    if dimension == 'T1': # for M1D format
        dimension = 2
    elif dimension == 'T3': # for MM1D format
        dimension = 3 #FIXME: is dimension always 3 for MM1D format?
    else:
        dimension = int(dimension)

    axis_units = {}
    
    # initialize units dictionary with None for all axes
    for i in range(1, dimension+1):
        axis_units[str(i)] = None

    # 
    axis_unit_line_pattern = re.compile(r"#\s*axis(\d+)_unit\s*=\s*(.+)")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and line.startswith("#"):

                # Extract table unit
                if line.startswith("# table_unit"):
                    table_unit = line.split("=", 1)[1].strip()
                
                # Extract axis units using regex
                m = axis_unit_line_pattern.match(line)
                if m:
                    axis_units[m.group(1)] = m.group(2)
            else:
                break  # stop reading after the header section

    #print(f"Extracted units dictionary: {axis_units}")
    reversed_axis_units = reverse_dimension_units(axis_units)
    #print(f"Reversed units dictionary: {reversed_axis_units}")
    return dimension, reversed_axis_units, table_unit


# Usage
if __name__ == "__main__":
    file_path1 = "sample_formats/data/3D.data"
    output = parse_header_of_data_file(file_path1)
    print(output)
    file_path2 = "sample_formats/data/2D.data"
    output = parse_header_of_data_file(file_path2)
    print(output)
    file_path3 = "sample_formats/data/M1D.data"
    output = parse_header_of_data_file(file_path3)
    print(output)
    file_path4 = "sample_formats/data/MM1D.data"
    output = parse_header_of_data_file(file_path4)
    print(output)