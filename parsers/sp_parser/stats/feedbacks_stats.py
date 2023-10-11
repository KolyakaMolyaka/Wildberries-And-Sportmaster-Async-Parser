from parsers.utilities.utils import get_json_from_file


def main():
	dataset = get_json_from_file('catalog-muzhskaya_obuv-krossovki')
	print('Feedbacks:', len(dataset))


if __name__ == '__main__':
	main()
