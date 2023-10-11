import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
import asyncio
from parsers.utilities.timer import Timer
from parsers.utilities import save_json_to_file
import aiohttp
from constants import COOKIES, HEADERS
from parsers.sp_parser.entities.pages_parser import PagesParser


async def main(url: str, pages: int):
	async with aiohttp.ClientSession(cookies=COOKIES, headers=HEADERS) as session:
		feedbacks = await PagesParser.parse_pages(session, url, pages)
		return feedbacks


if __name__ == '__main__':
	url = input('Введите ссылку на каталог для парсинга (например, "/catalog/zhenskaya_odezhda/kurtki/"): ')
	pages = int(input('Введите кол-во страниц, необходимых для парсинга (например, "2"): '))
	with Timer() as _:
		feedbacks = asyncio.run(main(url, pages))

	filename = '-'.join(url[1:-1].split('/')[1:])
	save_json_to_file([f for f in feedbacks], filename)
