from parser import parse_file


def generate_diff(file1, file2):
    file1 = parse_file(file1)
    file2 = parse_file(file2)

    keys_set = sorted(set(file1.keys()).union(set(file2.keys())))

    res = '{\n'
    for key in keys_set:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if value2 is None:
            res += f'  - {key}: {str(value1)}\n'
        elif value1 is None:
            res += f'  + {key}: {str(value2)}\n'
        else:
            if value1 == value2:
                res += f'    {key}: {str(value1)}\n'
            else:
                res += f'  - {key}: {str(value1)}\n'
                res += f'  + {key}: {str(value2)}\n'
    res += '}'
    return res
