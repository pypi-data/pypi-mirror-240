import requests

from PIL import Image
from io  import BytesIO


class Image:
	def __init__(self):
		self.img = None  # Pil Image

	def from_file(self, image_path):
		self.img = Image.open(image_path)
		return self

	def from_url(self, url):
		response = requests.get(url)
		self.img = Image.open(BytesIO(response.content))
		return self

	def from_base64(self, base64):
		image_bytes = base64.b64decode(base64_str)
		image_buf   = BytesIO(image_bytes)
		self.img    = Image.open(image_buf)
		return self

	def to_base64(self, image_path):
		with open(image_path, "rb") as f:
	    	return base64.b64encode(f.read())
	    return self

	def to_file(self, image_path):
		self.img.save(image_path)
		return self