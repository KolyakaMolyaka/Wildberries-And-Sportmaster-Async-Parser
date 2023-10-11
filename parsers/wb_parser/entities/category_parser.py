from parsers.wb_parser.entities.category import Category
from parsers.wb_parser.entities.pages_parser import PagesParser
from parsers.wb_parser.entities.products_parser import ProductsParser


class CategoryParser:
	@staticmethod
	async def parse(category: Category, session, pages: int = 10):
		""" Парсинг категории, у которых нет подкатегорий """
		assert not category.has_subcategories
		shard = category.shard
		cat_id = category.id

		# Парсинг страниц с продуктами
		parsed_pages = await PagesParser.parse_pages(session, shard, cat_id, pages)
		products = (prod for page in parsed_pages for prod in page['data']['products'])

		# Парсинг комментариев в карточках продукта
		feedbacks = await ProductsParser.parse_products(session, products)

		return feedbacks
