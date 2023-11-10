import openai

GPT_35_TURBO = {
	'model'        : 'gpt-3.5-turbo',
	'input_price'  : 0.001,
	'output_price' : 0.002,
	'token_limit'  : 4096,
}

GPT_35_TURBO_INSTRUCT = {
	'model'        : 'gpt-3.5-turbo-instruct',
	'input_price'  : 0.0015,
	'output_price' : 0.002,
	'token_limit'  : 4096,
}

GPT_40 = {
	'model'        : 'gpt-4',
	'input_price'  : 0.03,
	'output_price' : 0.06,
	'token_limit'  : 4096,
}

GPT_40_TURBO = {
	'model'        : 'gpt-4-1106-preview',
	'input_price'  : 0.01,
	'output_price' : 0.03,
	'token_limit'  : 4096,
}

GPT_40_TURBO_VISION = {
	'model'        : 'gpt-4-1106-vision-preview',
	'input_price'  : 0.01,
	'output_price' : 0.03,
	'token_limit'  : 4096,
}

GPT_40_32K = {
	'model'        : 'gpt-4-32k',
	'input_price'  : 0.06,
	'output_price' : 0.12,
	'token_limit'  : 4096,
}



class BaseModel:
	def __init__(self, model, conversation, api_key, temperature=0):
		self.api_key       = api_key
		openai.api_key     = api_key
		self.conversation  = conversation
		self.endpoint      = 'https://api.openai.com/v1/chat/completions'
		self.model         = model

		self.temperature   = temperature
		self.token_buffer  = 200

		self.input_tokens  = 0
		self.output_tokens = 0
		self.messages      = []

	def _update_usage(self, usage):
		self.input_tokens  += usage['prompt_tokens']
		self.output_tokens += usage['completion_tokens']

		if self.input_tokens + self.output_tokens >= self.model.token_limit - self.token_buffer:
			if len(self.messages) > 4:
				self.messages.pop(2)
				self.messages.pop(2)

	######################### PUBLIC #########################

	def name(self):
		return self.model.model

	def get_usage(self):
		price = 0
		price += self.input_tokens  * self.model.input_price / 1000
		price += self.output_tokens * self.model.output_price / 1000
		return price, self.input_tokens + self.output_tokens

	def unwind(self):
		if self.messages:
			while self.messages[-1]['role'] != 'system':
				self.messages.pop()

	def start(self, instructions=None):
		instructions = instructions if instructions else []
		for instruction in instructions:
			self.prompt(instruction, 'system')

	def prompt(self, content, role='user'):
		self.messages.append({'role': role, 'content': content})
		response = openai.ChatCompletion.create(
			model    = self.model,
			messages = self.messages
		)
		self._update_usage(response['usage'])
		choice = response['choices'][0]
		if choice['finish_reason'] != 'stop':
			raise Exception('Finish reason is ' + choice['finish_reason'])
		message = choice['message']
		self.messages.append(message)
		self.conversation.client.prompt(message['content'])
		return message['content']











