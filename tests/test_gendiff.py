from gendiff.scripts.gendiff import generate_diff


path1_json = './tests/fixtures/file1.json'
path2_json = './tests/fixtures/file2.json'
path1_yaml = './tests/fixtures/file1.yaml'
path2_yaml = './tests/fixtures/file2.yaml'
plain_fixture_path = './tests/fixtures/expected_plain_output.txt'
stylish_fixture_path = './tests/fixtures/expected_stylish_output.txt'
json_fixture_path = './tests/fixtures/expected_json_output.json'

with open(plain_fixture_path, 'r', encoding="utf-8") as file:
    plain_expected = file.read().strip()


def test_gendiff_plain_json():
    got = generate_diff(path1_json, path2_json, 'plain')
    assert got == plain_expected


def test_gendiff_plain_yaml():
    got = generate_diff(path1_yaml, path2_yaml, 'plain')
    assert got == plain_expected


with open(stylish_fixture_path, 'r', encoding="utf-8") as file:
    stylish_expected = file.read().strip()


def test_gendiff_stylish_json():
    got = generate_diff(path1_json, path2_json)
    assert got == stylish_expected


def test_gendiff_stylish_yaml():
    got = generate_diff(path1_yaml, path2_yaml)
    assert got == stylish_expected


with open(json_fixture_path, 'r', encoding='utf-8') as f:
    json_expected = f.read().strip()


def test_gendiff_json_json():
    got = generate_diff(path1_json, path2_json, 'json')
    assert got == json_expected


def test_gendiff_json_yaml():
    got = generate_diff(path1_yaml, path2_yaml, 'json')
    assert got == json_expected
