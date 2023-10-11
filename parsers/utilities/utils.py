__all__ = ['generate_fake_headers',
		   'get_json_by_url',
		   'save_json_to_file',
		   ]

import requests
from fake_headers import Headers
import json


def generate_fake_headers():
	""" Возвращает случайно сгенерированные заголовки """
	return Headers().generate()


def get_json_by_url(url: str):
	""" Возвращает JSON, полученный по ссылке """
	response = requests.get(url, headers=generate_fake_headers())
	status = response.status_code
	if status != 200:
		raise Exception(f'Не удалось загрузить JSON по ссылке {url}. Код ответа сервера = {status}. Ожидался 200.')
	return response.json()


def save_json_to_file(json_data, filename: str, ext='json', mode='w'):
	"""
	Сохранение JSON в файл
	filename - имя файла, например, main_menu (расширение указывать не нужно)
	ext - расширение файла, по умолчанию 'json'
	mode - режим открытия файла
	iterable_as_array - принимает Generator в качестве json_data
	"""

	with open(filename + f'.{ext}', mode, encoding='utf-8') as f:
		json.dump(json_data, f, ensure_ascii=False, indent=4)


def get_json_from_file(filename: str, ext='json'):
	"""
	Возвращает JSON из файла
	filename - имя файла, например, main_menu
	ext - расширение файла, по умолчанию 'json'

	"""

	with open(filename + f'.{ext}', 'r', encoding='utf-8') as f:
		d = json.load(f)

	return d
