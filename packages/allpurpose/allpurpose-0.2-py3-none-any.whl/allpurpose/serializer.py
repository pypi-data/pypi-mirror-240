import pickle
import hashlib

class Serializer:

	@staticmethod
	def signature(o):
		s = Serializer.serialize(o)
		return hashlib.md5(s).hexdigest()

	@staticmethod
	def serialize(o):
		return pickle.dumps(o)

	@staticmethod
	def unserialize(s):
		return pickle.loads(s)
	
	@staticmethod
	def save(file_path, o):
		with open(file_path, 'wb') as file:
			pickle.dump(o, file, protocol=pickle.HIGHEST_PROTOCOL)

	@staticmethod
	def load(file_path):
		with open(file_path, 'rb') as file:
			return pickle.load(file)
