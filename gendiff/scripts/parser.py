import json

def parse_file(path):
    f = json.load(open(path))
    return f

#print(parse_file('./file1.json'))