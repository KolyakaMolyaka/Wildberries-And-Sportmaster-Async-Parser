import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
import asyncio
import aiohttp
from parsers.wb_parser.entities.wbmenu import WbMenu
from parsers.wb_parser.entities.category_parser import CategoryParser
from parsers.utilities import save_json_to_file
from parsers.utilities.timer import Timer


async def main(menu: WbMenu, category_name: str, subcategory_name: str, pages=10):
	cat = menu.get_category(category_name)
	sc = cat.get_subcategory(subcategory_name)
	# sc = cat.get_subcategory('Брюки')
	async with aiohttp.ClientSession() as session:
		feedbacks = await CategoryParser.parse(sc, session, pages=pages)
		return feedbacks


if __name__ == '__main__':
	menu = WbMenu()
	menu.show()
	category_name = input('Введите название категории для парсинга (например, "Женщинам"): ')
	subcategory_name = input('Введите подкатегорию для парсинга (например, "Блузки и рубашки"): ')
	pages = int(input('Введите кол-во страниц (например, "2"): '))

	result_filename = category_name + '_' + subcategory_name
	with Timer() as _:
		feedbacks = asyncio.run(main(menu, category_name, subcategory_name, pages))

	save_json_to_file([f for f in feedbacks], result_filename)
