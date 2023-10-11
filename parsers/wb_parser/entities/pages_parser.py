import aiohttp
import asyncio

from parsers.utilities import generate_fake_headers


class PagesParser:
	class PageParser:
		@staticmethod
		async def parse_category_page(session, shard, cat_id, page):
			cat_catalog_url = fr'https://catalog.wb.ru/catalog/{shard}/catalog?TestGroup=no_filters_count&TestID=304&appType=1&cat={cat_id}&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,114&sort=popular&spp=27&page={page}'
			try:
				async with session.get(cat_catalog_url, headers=generate_fake_headers()) as r:
					if r.status == 200:
						return await r.json()
			except aiohttp.ContentTypeError:
				return None

	@staticmethod
	async def parse_pages(session, shard: str, cat_id: int, pages: int = 10):
		tasks = []
		for page in range(1, pages + 1):
			task = asyncio.create_task(PagesParser.PageParser.parse_category_page(session, shard, cat_id, page))
			tasks.append(task)

		parsed_pages = await asyncio.gather(*tasks)
		parsed_pages = filter(lambda p: p is not None, parsed_pages)
		return parsed_pages
