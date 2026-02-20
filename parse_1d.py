def parse_m1d_data_file(file_path):
    result = []

    with open(file_path, "r", encoding="utf-8") as f:
        col1 = []
        col2 = []
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                a, b = map(float, line.split())
                col1.append(a)
                col2.append(b)
            
        result = [col1, col2]

    #print(result)
    return result

   
# Usage
if __name__ == "__main__":
    file_path = "sample_formats/data/1D.data"
    output = parse_m1d_data_file(file_path)
    print(output)