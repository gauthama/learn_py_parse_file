



# Sample header content:
    # Table format: 2D
    # table_unit = Ohm
    # axis1_unit = degC
    # axis2_unit = %

#from learn_py_parse_file.parse_data_file import extract_dim_from_header
from parse_data_file import extract_dim_from_header
import re

def extract_units_using_regular_expressions(file_path):
    #import re

    units = {}

    pattern = re.compile(r"#\s*axis(\d+)_unit\s*=\s*(.+)")

    with open("data.txt") as f:
        for line in f:
            m = pattern.match(line)
            if m:
                units[m.group(1)] = m.group(2)

def get_dimension_from_data_file(file_path):
    first_line = open(file_path, "r", encoding="utf-8").readline().rstrip("\n")
    prefix = "# Table format: "
    suffix = "D"
    dimension = extract_dim_from_header(first_line, prefix, suffix)
    return dimension

def parse_header_of_data_file(file_path):
    dimension = get_dimension_from_data_file(file_path)

    units = {}

    # initialize units dictionary with None for all axes
    for i in range(1, int(dimension)+1):
        units[str(i)] = None

    # 
    unit_line_pattern = re.compile(r"#\s*axis(\d+)_unit\s*=\s*(.+)")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and line.startswith("#"):

                # Solution using string methods
                # # remove leading '#'
                # content = line[1:].strip()

                # if content.startswith("axis") and "_unit" in content:
                #     left, right = content.split("=", 1)
                #     axis_num = left.replace("axis", "").replace("_unit", "").strip()
                #     unit = right.strip()

                #     units[axis_num] = unit

                # Solution using regular expressions
                m = unit_line_pattern.match(line)
                if m:
                    units[m.group(1)] = m.group(2)
            else:
                break  # stop reading after the header section
    return dimension,units


# Usage
if __name__ == "__main__":
    file_path1 = "sample_formats/data/3D.data"
    output = parse_header_of_data_file(file_path1)
    print(output)
    file_path2 = "sample_formats/data/2D.data"
    output = parse_header_of_data_file(file_path2)
    print(output)