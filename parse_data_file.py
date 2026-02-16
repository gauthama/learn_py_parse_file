# Open and read a text file line by line


file_path = "sample_formats/data/2D.data"
prefix = "# Table format: "
suffix = "D"


import re


def extract_dim_using_regex(file_path):
    pattern = r"^# Table format: (.+)D$"

    with open(file_path, "r", encoding="utf-8") as f:
        header = f.readline().strip()

    match = re.match(pattern, header)
    if not match:
        raise ValueError("Invalid table format header")

    value = match.group(1)
    print(value)




def extract_dim_from_header(header, prefix, suffix):
    print(f"Header: {header.strip()}")
    header = header.strip()  # remove leading/trailing whitespace
    if header.startswith(prefix) and header.endswith(suffix):
        value = header[len(prefix):-len(suffix)]  # remove prefix and trailing suffix    
    else:
        raise ValueError("Invalid table format header")

    print(f"Extracted value (Dimension): {value}")
    return value



def process_data_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == 0:
                value = extract_dim_from_header(line, prefix, suffix)
                continue

        # process remaining lines here
            print(line.strip())

process_data_file(file_path)
extract_dim_using_regex(file_path)

# def new_func(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 print(line.rstrip('\n'))
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")

# new_func(file_path)