

def parse_m1d_data_file(file_path):
    result = [[], []]

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # skip empty lines and comments
            if not line.strip() or line.startswith("#"):
                continue

            a, b = map(float, line.split())
            result[0].append(a)
            result[1].append(b)

    print(result)
    return result



# Usage
if __name__ == "__main__":
    file_path = "sample_formats/data/M1D_tiny.data"
    output = parse_m1d_data_file(file_path)
    print(output)  # [[0, 7, 1], [2, 5, 3]]