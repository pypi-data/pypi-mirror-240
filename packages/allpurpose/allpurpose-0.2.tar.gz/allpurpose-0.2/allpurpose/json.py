from datetime import datetime
import json
import os

from web.apps import WebConfig

class Json:

	@staticmethod
	def _path(file_path):
		if not os.path.exists(file_path):
			file_path = os.path.join(WebConfig.DATA_PATH, file_path)
			if not os.path.exists(file_path):
				raise FileNotFoundError(f'File not found neither locally nor in data/: {file_path}')
		return file_path

	@staticmethod
	def serialize(o):
		return json.dumps(o, default=Json.datetime_to_str)

	@staticmethod
	def deserialize(s):
		return json.loads(s)


	@staticmethod
	def load(file_path):
		file_path = Json._path(file_path)
		with open(file_path) as f:
			return Json.deserialize(f.read())

	@staticmethod
	def save(file_path, o, in_data_folder=False):
		if in_data_folder:
			file_path = os.path.join(WebConfig.DATA_PATH, file_path)
		with open(file_path, 'w') as f:
			return f.write(Json.serialize(o))

	@staticmethod
	def datetime_to_str(obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		return obj
