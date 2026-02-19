# Open and read a text file line by line


file_path = "sample_formats/data/2D.data"
prefix = "# Table format: "
suffix = "D"


# import re


# def extract_dim_using_regex(file_path):
#     pattern = r"^# Table format: (.+)D$"

#     with open(file_path, "r", encoding="utf-8") as f:
#         header = f.readline().strip()

#     match = re.match(pattern, header)
#     if not match:
#         raise ValueError("Invalid table format header")

#     value = match.group(1)
#     print(value)


# Input: [[0.0, 50.0], [0.0, 5.0, 10.0, 15.0], [0.0, 25.0, 50.0]]
# Output{'D1': [0.0, 25.0, 50.0], 'D2': [0.0, 5.0, 10.0, 15.0], 'D3': [0.0, 50.0]}

def process_dimension_data(dim_data_matrix):
    dim_data_dict = {}
    for i, values in enumerate(reversed(dim_data_matrix)):
        dim_key = f"D{i+1}"
        dim_data_dict[dim_key] = values
    #print(f"Processed dimension data dictionary: {dim_data_dict}")
    return dim_data_dict


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
    values = []
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            # Extract dimension from the header line
            if i == 0:
                dim_value = extract_dim_from_header(line, prefix, suffix)
                dim_value = int(dim_value)  # convert dimension value to integer
                continue
            
            # skip empty lines and comments
            if not line.strip() or line.startswith("#"):
                continue  
            
            # Convert the line into a list of floats
            num_list = [float(x) for x in line.split()]
            #print(f"Extracted values from line {i+1}: {num_list}")
            values.append(num_list)
            

    #print(f"Extracted values from file: {values}")
    dim_list = values[:dim_value]
    dim_list = [int(x[0]) for x in dim_list]
    # extract dimension matrix from the file data
    dim_data_matrix = values[dim_value: dim_value + dim_value]
    data_matrix = values[dim_value + dim_value:]

    print(f"Extracted dimension list: {dim_list}")
    print(f"Extracted dimension data matrix: {dim_data_matrix}")
    #print(f"Extracted data matrix: {data_matrix}")

    dim_data_dict = process_dimension_data(dim_data_matrix)
    print(f"Dimension data dictionary: {dim_data_dict}")
    

process_data_file(file_path)
# extract_dim_using_regex(file_path)

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