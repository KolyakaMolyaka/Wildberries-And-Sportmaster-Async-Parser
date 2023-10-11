from parsers.sp_parser.constants import *
from bs4 import BeautifulSoup as Bs


class FeedbackParser:
	@staticmethod
	async def parse_feedback(session, product_id: int, page: int):
		url = rf"https://w-api2.aplaut.io/widgets/56fa337b8ddf870c76021a5f/v3/product/{product_id}/product-reviews.html?hostname=sportmaster.ru&page={page}"

		print(f'> Parsing feedbacks of product id={product_id} on page={page}; url = {url}')
		async with session.get(
				url,
				cookies=COOKIES,
				headers=HEADERS,
		) as r:
			html_doc = await r.text()

		soup = Bs(html_doc, 'lxml')
		review_container = soup.find('div', class_='sp-reviews-wrap')

		if not review_container:
			print(fr'https://www.sportmaster.ru/product/{product_id}/ has no reviews.')
			return

		feedbacks = []
		reviews = review_container.find_all(attrs={'itemprop': 'review'})
		for r in reviews:
			author = r.find(attrs={'itemprop': 'author'}).text.strip()
			stars = len(r.find_all(class_='sp-star-on'))
			date = r.find(attrs={'itemprop': 'datePublished'}).text.strip()
			# Парсинг достоинства, недостатка, комментария
			review_container = r.find(attrs={'itemprop': 'reviewBody'})

			comments = []
			for review_line in review_container.find_all(class_='sp-review-content-item'):
				if not review_line.text.strip():
					continue

				label_tag = review_line.find(class_='sp-review-content-label')
				label = label_tag.text.strip()
				comment = label_tag.next_sibling.text.strip()
				comments.append({label: comment})

			details = []
			for detail, about in zip(
					review_container.find_all(class_='sp-review-detail-name'),
					review_container.find_all(class_='sp-review-detail-value')
			):
				details.append({detail.text.strip(): about.text.strip()})

			feedbacks.append({
				'author': author,
				'starts': stars,
				'date': date,
				'comments': comments,
				'details': details,
				'url': fr'https://www.sportmaster.ru/product/{product_id}/'
			})

		return (f for f in feedbacks) if feedbacks else None
