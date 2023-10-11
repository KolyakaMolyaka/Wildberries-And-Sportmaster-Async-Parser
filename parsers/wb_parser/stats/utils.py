
def get_frequently_encountered_words(feedbacks: dict, limit=10, min_word_length=3, exclude=None):
	"""
	 Возвращает список самых встречающихся слов в отзывах
	 limit - количество возвращаемых слов (ТОП <limit>)
	 min_word_length - минимальная длина учитываемого слова
	 exclude - список символов, который не будут считаться
	 """
	if not exclude:
		exclude = list(',.?!#:;$%@*()^<>/+-\\')
	top_words = dict()
	for f in feedbacks:
		words = [w.lower().strip(''.join(exclude)) for w in map(str.strip, f.split()) if
				 w not in exclude and len(w) > min_word_length]
		for w in words:
			if w in top_words:
				top_words[w] += 1
			else:
				top_words[w] = 1
	sorted_top_words = sorted(top_words.items(), key=lambda i: -i[1])
	return sorted_top_words[:limit]


def group_by_feedback_value(feedbacks: dict):
	""" Разбивает комментарии по оценке """
	res = {}
	for f in feedbacks:
		valuation = str(f['valuation'])
		if valuation not in res:
			res[valuation] = [f]
		else:
			res[valuation].append(f)
	return res
