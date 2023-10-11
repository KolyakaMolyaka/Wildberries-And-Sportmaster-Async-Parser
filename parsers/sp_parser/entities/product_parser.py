import asyncio

from parsers.sp_parser.entities.feedbacks_parser import FeedbacksParser


class ProductParser:
	@staticmethod
	async def parse_products(session, products):
		tasks = []
		for product in products:
			product_id = product['productId']
			task = asyncio.create_task(FeedbacksParser.parse_feedbacks(session, product_id))
			tasks.append(task)

		feedbacks = await asyncio.gather(*tasks)
		# Объедиенние комментариев по товарам в один генератор
		feedbacks = (f for f_prod in feedbacks for f in f_prod)
		return feedbacks

