import asyncio

from parsers.sp_parser.entities.page_parser import PageParser


class PagesParser:
	""" Парсер страниц указанной категории по url """

	@staticmethod
	async def parse_pages(session, url: str, pages: int):
		tasks = []
		for page in range(1, pages + 1):
			task = asyncio.create_task(PageParser.parse_page(session, url, page))
			tasks.append(task)
		feedbacks = await asyncio.gather(*tasks)
		# Объединение комментариев по страницам категории в один генератор
		feedbacks = (f for f_page in feedbacks for f in f_page)
		return feedbacks
