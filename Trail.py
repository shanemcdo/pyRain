import sys
import random
import colorama
colorama.init()

class Trail:

	def __init__(self, x, y, char_list = None, index = 0):
		self.x = x
		self.y = y
		if char_list == None:
			self.list = Trail.get_char_list()
		else:
			self.list = char_list
	
	def draw(self):
		Trail.gotoxy(self.x, self.y)
		print(self.list[0])

	@staticmethod
	def get_char_list():
		return [Trail.get_random_char() for i in range(0, random.randint(5,10))]
	
	@staticmethod
	def get_random_char():
		options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		return random.choice(options)

	@staticmethod
	def gotoxy(x, y):
		sys.stdout.write(f"\033[{y};{x}H")
		sys.stdout.flush()
