from parsers.utilities.utils import get_json_from_file
from parsers.wb_parser.stats.utils import (
	get_frequently_encountered_words,
	group_by_feedback_value
)


def frequently_encountered_words_dialog(feedbacks):
	limit = int(input('ТОП-? популярных слов вас устроит (число)?: '))
	for index, (word, frequency) in \
			enumerate(get_frequently_encountered_words([f['text'] for f in feedbacks], limit=limit)):
		print(f'{index + 1}. <{word}>', 'occur', frequency, 'time(s).')


def print_feedbacks_in_brief(feedbacks):
	feedback_len = int(input('Какая макс. длина отзыва вас устроит (для укорочения вывода)?: '))
	limit = int(input('Сколько отзывов хотите вывести?: '))
	for f in feedbacks[:limit]:
		print(f['valuation'], '|',
			  f['text'][:feedback_len] + '...' if len(f['text']) > feedback_len else f['text'][:feedback_len])


def grouped_feedbacks_dialog(feedbacks):
	grouped_feedbacks = group_by_feedback_value(feedbacks)
	req_valuation = input('Какие оценки вас интересуют (1-5): ')
	req_limit = int(input('Сколько оценок вы хотели бы вывести (макс. число)?: '))
	for f in grouped_feedbacks[req_valuation][:req_limit]:
		print('Оценка:', f['valuation'], '\nОтзыв:', f['text'])
		print()


def main():
	# feedbacks = get_json_from_file('parsed_feedbacks')
	feedbacks = get_json_from_file('../parsed1')
	print('Feedbacks number: ', len(feedbacks))

	# Choose one of this
	# grouped_feedbacks_dialog(feedbacks)
	# frequently_encountered_words_dialog(feedbacks)
	# print_feedbacks_in_brief(feedbacks)

if __name__ == '__main__':
	main()
