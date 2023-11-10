import hashlib
import time

class Crypto:

	@staticmethod
	def md5(s=None):
		if s is None:
			s = str(time.time())
		return hashlib.md5(s.encode()).hexdigest()