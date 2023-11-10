import os
import requests
import openai

from library.string import String


class Dalle:
	SIZE_LARGE  = '1024x1024'
	SIZE_MEDIUM = '512x512'
	SIZE_SMALL  = '256x256'

	def __init__(self, api_key):
		openai.api_key = api_key
		self.images = []

	def images(self, prompt, size, quantity=1, base64=False):
		print(f'Dall-E generating image for "{prompt}"')
		if quantity < 0  : quantity = 0
		if quantity > 10 : quantity = 10

		response = openai.Image.create(
		  prompt = prompt,
		  n      = quantity,
		  size   = size
		)

		return response['data'], prompt