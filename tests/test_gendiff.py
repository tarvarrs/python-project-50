from gendiff.scripts.gendiff import generate_diff


path1_json = './tests/fixtures/file1.json'
path2_json = './tests/fixtures/file2.json'
path1_yaml = './tests/fixtures/file1.yaml'
path2_yaml = './tests/fixtures/file2.yaml'


# with open('./tests/fixtures/expected_plain_output.txt', 'r', encoding="utf-8") as file:
#     expected = file.read()


# def test_gendiff_plain_json():
#     got = generate_diff(path1_json, path2_json)
#     assert got == expected


# def test_gendiff_plain_yaml():
#     got = generate_diff(path1_yaml, path2_yaml)
#     assert got == expected


with open('./tests/fixtures/expected_stylish_output.txt', 'r', encoding="utf-8") as file:
    expected = file.read().strip()


def test_gendiff_stylish_json():
    got = generate_diff(path1_json, path2_json)
    assert got == expected


def test_gendiff_stylish_yaml():
    got = generate_diff(path1_yaml, path2_yaml)
    assert got == expected
