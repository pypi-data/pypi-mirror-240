import sys

from colors import Colors


class PeerError(Exception):
	def __init__(self, message='Peer error'):
		super().__init__(message)

	@staticmethod
	def exit(message='Critical error.', code=2):
		print(f'{Colors.RED}{message}{Colors.RESET}', file=sys.stderr)
		sys.exit(code)
