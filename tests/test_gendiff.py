from gendiff.scripts.generate_diff import generate_diff

with open('./tests/fixtures/expected_output.txt', 'r', encoding="utf-8") as file:
    expected = file.read()


def test_gendiff_json():
    got = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    assert got == expected


def test_gendiff_yaml():
    got = generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yaml')
    assert got == expected


with open('./tests/fixtures/expected_tree_output.txt', 'r', encoding="utf-8") as file:
    expected = file.read()


def test_gendiff_tree_json():
    got = generate_diff('./tests/fixtures/file1_tree.json', './tests/fixtures/file2_tree.json')
    assert got == expected


def test_gendiff_tree_yaml():
    got = generate_diff('./tests/fixtures/file1_tree.yaml', './tests/fixtures/file2_tree.yaml')
    assert got == expected
