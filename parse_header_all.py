from parse_data_file import extract_dim_from_header
import re


def get_dimension_from_data_file(file_path):
    first_line = open(file_path, "r", encoding="utf-8").readline().rstrip("\n")
    prefix = "# Table format: "
    suffix = "D"
    dimension = extract_dim_from_header(first_line, prefix, suffix)
    return dimension


def add_prefix_to_dictionary_keys(input_dict, prefix="D"):
    result = {}
    for key in list(input_dict.keys()):
        result[f"{prefix}{key}"] = input_dict[key]

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

    axis_tokens = {}
    # initialize tokens dictionary with None for all axes
    for i in range(1, dimension + 1):
        axis_tokens[str(i)] = None

    #
    axis_unit_line_pattern = re.compile(r"#\s*axis(\d+)_unit\s*=\s*(.+)")
    axis_token_line_pattern = re.compile(r"#\s*axis(\d+)_token\s*=\s*(.+)")

    #
    other_comments = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and line.startswith("#"):

                other_comment_flag = True

                # Extract table unit
                if line.startswith("# table_unit"):
                    table_unit = line.split("=", 1)[1].strip()
                    other_comment_flag = False

                # Extract axis units using regex
                m = axis_unit_line_pattern.match(line)
                if m:
                    axis_units[m.group(1)] = m.group(2)
                    other_comment_flag = False

                # Extract axis tokens using regex
                m = axis_token_line_pattern.match(line)
                if m:
                    axis_tokens[m.group(1)] = m.group(2)
                    other_comment_flag = False
                
                # Collect other comments
                if other_comment_flag and not line.startswith("# Table format:"):
                    comment = line[1:].strip()  # remove leading '#' and strip whitespace
                    if comment:  # only add non-empty comments  
                        other_comments.append(comment)
            else:
                break  # stop reading after the header section

    axis_units = add_prefix_to_dictionary_keys(axis_units, prefix="X")
    axis_tokens = add_prefix_to_dictionary_keys(axis_tokens, prefix="X")

    return {
        'table_unit': table_unit,
        'axis_units': axis_units,
        'axis_tokens': axis_tokens,
        'comments': other_comments
    }


# Usage
if __name__ == "__main__":
    file_path1 = "sample_formats/data/MM1D.data"
    output = parse_header_of_data_file(file_path1)
    print(output)
 