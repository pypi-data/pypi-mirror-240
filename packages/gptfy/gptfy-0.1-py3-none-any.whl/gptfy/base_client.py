from settings        import *
from allpurpose.file import File
from peer_error      import PeerError


class BaseClient:
	def __init__(self, conversation, name):
		self.conversation      = conversation
		self.name              = name
		self.path              = File.path('clients', name)
		self.instructions_path = File.path(self.path, INSTRUCTIONS_DIR_NAME)

		if not File.exists(self.instructions_path):
			PeerError.exit('Instructions directory does not exist')

	def get_instructions(self):
		instructions = []
		for file_name in File.list_files(self.instructions_path, ['txt']):
			instructions.append(File.read(File.path(self.instructions_path, file_name)))

		if len(instructions) == 0:
			PeerError.exit('No txt instructions present in instructions directory')
		return instructions


	def start(self):
		...

	def prompt(self, content):
		...