from allpurpose.file   import File
from allpurpose.module import Module


class Conversation:
	def __init__(self, api_key, model, client_name):
		model_class  = Module.imp_class(File.path('models', model_name))
		client_class = Module.imp_class(File.path('clients', client_name, 'client'))

		self.model  = model_class(model, self, api_key)
		self.client = client_class(self, client_name)

	def start(self):
		print('Connected to ' + self.model.name())
		instructions = self.client.get_instructions()
		self.model.start(instructions)
		self.client.start(self.prompt)

	def prompt(self, prompt):
		return self.model.prompt(prompt)