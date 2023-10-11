from time import time


class Timer:
	def __init__(self, round=2):
		self._round = round

	def __enter__(self):
		self._start = time()

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self._delta_secs = round(time() - self._start, self._round)
		self._delta_mins = round(self._delta_secs / 60, self._round)
		print('Time: %s sec(s) ~ %s min(s)' % (self._delta_secs, self._delta_mins))
