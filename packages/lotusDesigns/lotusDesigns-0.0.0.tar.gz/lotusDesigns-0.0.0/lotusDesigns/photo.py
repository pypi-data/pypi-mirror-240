"""Photo manipulation."""

import copy
import imageio
import numpy as np
from PIL import Image
from PIL import ImageOps


class Photo:
	"""Class that represents a photograph."""

	def __init__(self, image):
		"""Initialise a photograph."""
		if isinstance(image, str):
			# Read from image path
			self.image = imageio.imread(image, pilmode='RGBA')

			# Convert to PIL image
			self.image = Image.fromarray(self.image)
		else:
			# Read from PIL image
			self.image = image.convert("RGBA")

	def __str__(self):
		"""Print photo attributes."""
		s = ""
		if not isinstance(self.image, Image.Image):
			s += "Not a PIL image"
		else:
			s += f" Mode: {self.image.mode}"
			s += f" Size: {self.image.size}"
			image = np.array(self.image)
			s += f" Shape: {image.shape}"
		return s

	def copy(self):
		"""Copy the photo."""
		return copy.deepcopy(self)

	def save(self, path):
		"""Save the photo."""
		self.image.convert('RGB').save(path)

	def addOverlay(self, photo, x, y):
		"""Merge the photo."""
		w = self.image.size[0]
		h = self.image.size[1]

		image = Image.new("RGBA", (w, h))
		image.paste(self.image, (0, 0), self.image)
		image.paste(photo.image, (x, y), photo.image)

		self.image = image

	def scale(self, width, height):
		"""Scale the photo."""
		self.image = self.image.resize((width, height))

	def show(self):
		"""Show the photograph on screen."""
		self.image.show()
