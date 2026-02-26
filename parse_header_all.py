from parse_data_file import extract_dim_from_header
import re


def get_dimension_from_data_file(file_path):
    first_line = open(file_path, "r", encoding="utf-8").readline().rstrip("\n")
    prefix = "# Table format: "
    suffix = "D"
    dimension = extract_dim_from_header(first_line, prefix, suffix)
    return dimension


def dimension_units_add_prefix(units_dict):
    # build result dictionary
    result = {}
    for key in list(units_dict.keys()):
        result[f"X{key}"] = units_dict[key]

    return result


def parse_header_of_data_file(file_path):
    table_unit = None

    dimension = get_dimension_from_data_file(file_path)
    if dimension == 'T1':  # for M1D format
        dimension = 2
    elif dimension == 'T3':  # for MM1D format
        dimension = 3
    else:
        dimension = int(dimension)

    axis_units = {}

    # initialize units dictionary with None for all axes
    for i in range(1, dimension + 1):
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

    axis_units = dimension_units_add_prefix(axis_units)

    return {
        'table_unit': table_unit,
        'axis_units': axis_units,
        'axis_tokens': {},
        'comments': []
    }


# Usage
if __name__ == "__main__":
    file_path1 = "sample_formats/data/MM1D.data"
    output = parse_header_of_data_file(file_path1)
    print(output)

 