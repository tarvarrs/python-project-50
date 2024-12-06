def find_diff(data1, data2):
    keys_set = sorted(set(data1.keys()).union(set(data2.keys())))
    diff = {}

    for key in keys_set:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if value1 is None:
            diff[key] = ('added', value2)
        elif value2 is None:
            diff[key] = ('removed', value1)
        elif value1 == value2:
            diff[key] = ('unchanged', value1)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = ('nested', find_diff(value1, value2))
        else:
            diff[key] = ('changed', (value1, value2))
    return diff
