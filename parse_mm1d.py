def parse_mm1d_data_file(file_path):
    mm_result = {}

    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            # Read block size (skip comments/empty lines)
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    tmp_list =line.split()
                    slice_group_value = tmp_list[0]
                    slice_count = int(float(tmp_list[1]))
                    break
            else:
                break  # EOF reached

            m_result = {}
            for _ in range(slice_count):
                # Read block size (skip comments/empty lines)
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        tmp_list =line.split()
                        slice_value = tmp_list[0]
                        count = int(float(tmp_list[1]))
                        break
                else:
                    raise ValueError("Unexpected EOF inside data block")

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

                m_result[slice_value] = [col1, col2]
            print(m_result)
            mm_result[slice_group_value] = m_result
    #print(mm_result)
    return mm_result

   
# Usage
if __name__ == "__main__":
    file_path = "sample_formats/data/MM1D.data"
    output = parse_mm1d_data_file(file_path)
    print()
    print(output)