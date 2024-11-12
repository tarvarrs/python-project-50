import argparse

parser = argparse.ArgumentParser(
	prog='gendiff', 
	usage='%(prog)s [-h] first_file second_file',
	description='Compares two configuration files and shows a difference.',
	formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
	parser.print_help()


if __name__ == 'main':
	main()
