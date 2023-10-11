import math
import asyncio
from bs4 import BeautifulSoup as Bs
from parsers.sp_parser.entities.feedback_parser import FeedbackParser
from parsers.sp_parser.constants import *


class FeedbacksParser:
	@staticmethod
	async def parse_feedbacks(session, product_id: int):
		url = rf"https://w-api2.aplaut.io/widgets/56fa337b8ddf870c76021a5f/v3/product/{product_id}/product-reviews.html?hostname=sportmaster.ru&page=1"

		async with session.get(
				url,
				cookies=COOKIES,
				headers=HEADERS,
		) as r:
			html_doc = await r.text()

		soup = Bs(html_doc, 'lxml')
		try:
			total_reviews = int(soup.find(attrs={'itemprop': 'reviewCount'}).text)
		except:
			total_reviews = 0

		reviews_pages = math.ceil(total_reviews / 4)

		tasks = []
		for page in range(1, reviews_pages + 1):
			task = asyncio.create_task(FeedbackParser.parse_feedback(session, product_id, page))
			tasks.append(task)

		feedbacks = await asyncio.gather(*tasks)
		# Очистка страниц с отсутствующими комментариями
		feedbacks = filter(bool, feedbacks)
		# Объединение всех комментариев в один генератор
		feedbacks = (f for f_page in feedbacks for f in f_page)
		return feedbacks
