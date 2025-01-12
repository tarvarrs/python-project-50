import argparse
from gendiff.scripts.parse_file import parse_file
from gendiff.scripts.find_diff import find_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_formatter

FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_formatter
}


def generate_diff(file1, file2, formatter='stylish'):
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    raw_diff = find_diff(data1, data2)
    if isinstance(formatter, str):
        formatter = FORMATTERS[formatter]
    diff = formatter(raw_diff)
    return diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='%(prog)s [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    formatter = args.format
    diff = generate_diff(file_path1, file_path2, formatter)
    print(diff)


if __name__ == 'main':
    main()
