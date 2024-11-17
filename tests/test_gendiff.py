from gendiff.scripts.generate_diff import generate_diff

with open('./tests/fixtures/expected_output.txt', 'r', encoding="utf-8") as file:
    expected = file.read()


def test_gendiff():
    got = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    assert got == expected