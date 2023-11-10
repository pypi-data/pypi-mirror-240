import json
import re

from library.file  import File
from library.image import Image


class ImageStore:
	def __init__(self, images_dir):
		self.db_path    = File.path(images_dir, 'db.json')
		self.images_dir = File.path(images_dir)

	def _normalize_key(self, key):
		return re.sub(r'\s+', '_', key).lower().strip()

	def _load_db(self):
		with open(self.db_path, 'a+') as f:
			f.seek(0)
			content = f.read()
			if len(content) > 0:
				return json.loads(content)
		return {}

	def _save_db(self, db):
		with open(self.db_path, 'w') as f:
			f.write(json.dumps(db))

	####################### PUBLIC #######################

	def get(self, key):
		key = self._normalize_key(key)
		db  = self._load_db()

		if key in db:
			return File.path(self.images_dir, db[key])
		return None

	def set(self, key, file_name):
		key = self._normalize_key(key)
		db  = self._load_db()

		if key not in db:
			db[key] = []

		db[key].append(file_name)
		self._save_db(db)

	def download(self, urls, key):
		image_base_name = String.random_hex(8)
		for n, url in enumerate(urls):
			image_name = File.path(self.images_dir, f'{image_base_name}_{n}.webp')
			Image().from_url(url).to_file(image_name)
			self.set(key, image_name)








