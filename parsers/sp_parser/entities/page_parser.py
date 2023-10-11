from parsers.sp_parser.constants import *

from parsers.sp_parser.entities.product_parser import ProductParser


class PageParser:
	@staticmethod
	async def parse_page(session, url: str, page: int):
		json_data = {
			'url': url,
			'page': page + 1,
		}
		async with session.post('https://www.sportmaster.ru/web-api/v1/catalog/',
								json=json_data, headers=HEADERS, cookies=COOKIES) as r:
			page_json = await r.json()

		feedbacks = await ProductParser.parse_products(session, page_json['products'])
		return feedbacks
