from .exceptions import NoShardTagInCategoryExc
class Category:
	""" Категория меню Wildberries. Может содержать подкатегории. """

	def __init__(self, cat: dict):

		if 'shard' not in cat:
			raise NoShardTagInCategoryExc()

		if 'childs' in cat:
			self._has_subcategories = True

			self._subcategories = []
			for child in cat['childs']:
				sc = Category(child)
				self._subcategories.append(sc)
			del cat['childs']

		else:
			self._has_subcategories = False
		self._cat = cat

	@property
	def name(self):
		""" Возвращает название текущей категории """
		return self._cat['name']

	@property
	def shard(self):
		""" Возвращает shard текущей категории """
		return self._cat['shard']

	@property
	def id(self):
		""" Возвращает id текущей категории """
		return self._cat['id']

	@property
	def subcategories(self):
		""" Возвращает подкатегории текущей категории или пустой список """
		if self.has_subcategories:
			return (sc for sc in self._subcategories)
		return []

	@property
	def has_subcategories(self) -> bool:
		""" Проверяет, есть ли у текущей категории какие-либо подкатегории """
		return self._has_subcategories

	def has_category(self, category_name: str) -> bool:
		""" Проверяет, есть ли в текущей категории подкатегория с заданным именем """
		if self.has_subcategories:
			for c in self.subcategories:
				return c.has_category(category_name)
		return False

	def get_subcategory(self, category_name: str) -> 'Category' or None:
		""" Возвращает подкатегорию с заданным именем или None"""

		if not self.has_subcategories:
			return None

		try:
			cat = next(filter(lambda c: c.name == category_name, self.subcategories))
			return cat
		except StopIteration:
			return None

	def __repr__(self):
		return f"""\
		id: {self._cat['id']},
		name: {self._cat['name']},
		url: {self._cat['url']},
		"""
