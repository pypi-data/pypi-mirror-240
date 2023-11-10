from gptfy.model import Model


class Conversation:
	def __init__(self, api_key, model, client, instructions):
		self.model        = Model(model, self, api_key)
		self.client       = client
		self.instructions = instructions

	def start(self):
		print('Connected to ' + self.model.name())
		self.model.start(self.instructions)
		self.client.start(self.prompt)

	def prompt(self, prompt):
		return self.model.prompt(prompt)