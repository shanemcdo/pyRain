import sys
import random
import colorama
colorama.init()

class Trail:

	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self):
		pass
	
	@staticmethod
	def get_random_char():
		options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		return random.choice(options)

	@staticmethod
	def gotoxy(x, y):
		sys.stdout.write(f"\033[{x};{y}H")
		sys.stdout.flush()
