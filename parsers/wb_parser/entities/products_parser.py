import asyncio

from parsers.utilities import generate_fake_headers


async def pick_up_feedback_json(session, feedback_id: int):
	urls = (fr'https://feedbacks{i}.wb.ru/feedbacks/v1/{feedback_id}' for i in range(1, 10))

	for url in urls:
		try:
			async with session.get(url, headers=generate_fake_headers()) as resp:
				feedback_json = await resp.json()
				if not feedback_json['feedbacks']:
					continue
		except:
			pass
		else:
			return feedback_json

	return None


async def pick_up_product_card_json(session, prod_id: str):
	urls = (
		f'https://basket-{str(i).rjust(2, "0")}.wb.ru/vol{prod_id[:-5]}/part{prod_id[:-3]}/{prod_id}/info/ru/card.json'
		for
		i in range(1, 16))
	for url in urls:
		try:
			async with session.get(url, headers=generate_fake_headers()) as resp:
				prod_json = await resp.json()
		except:
			pass
		else:
			return prod_json

	return None


class ProductsParser:
	class ProductParser:
		@staticmethod
		async def parse_product(session, product):
			print(f'\t\t- Parse product: {product["name"]}')

			prod_id = str(product['id'])

			print(f'\t\t | Starting resolving feedbacks for {product["name"]}')
			prod_json = await pick_up_product_card_json(session, prod_id)
			feedback_id = prod_json['imt_id']
			feedback_json = await pick_up_feedback_json(session, feedback_id)
			no_feeds_url = f'https://www.wildberries.ru/catalog/{prod_id}/detail.aspx'
			if not feedback_json:
				print(f"\t\t !!! Error !!! No feedbacks at {no_feeds_url}")
			print(f'\t\t + Finished resolved feedbacks for {product["name"]}')

			if not feedback_json:
				return None
			elif feedback_json['feedbacks']:
				feedbacks = ({'text': f['text'], 'val': f['productValuation']} for f in feedback_json['feedbacks'])
				return feedbacks
			return None

	@staticmethod
	async def parse_products(session, products):
		tasks = []
		for prod in products:
			task = asyncio.create_task(ProductsParser.ProductParser.parse_product(session, prod))
			tasks.append(task)

		feedbacks = await asyncio.gather(*tasks)
		feedbacks = filter(bool, feedbacks)

		# Единый список комментариев
		feedbacks = (f for fgen in feedbacks for f in fgen)
		return feedbacks
