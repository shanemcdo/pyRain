import sys
import random
import colorama
colorama.init(autoreset = True)

class Trail:

	def __init__(self, width, height, x, y, char_list = None, index = 0):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		if char_list == None:
			self.list = self.get_char_list()
		else:
			self.list = char_list
		self.list_length = len(self.list)
		self.index = index

	def draw(self):
		if self.y > 0 and self.y < self.height:
			Trail.gotoxy(self.x, self.y)
			if self.index == 0:
				color = colorama.Fore.WHITE
			else:
				color = colorama.Fore.GREEN + colorama.Style.BRIGHT
			print(color + self.list[self.index])
		if self.index + 1 < self.list_length:
			Trail(self.width, self.height, self.x, self.y - 1, self.list, self.index + 1).draw()
		elif self.y - 1 > 0 and self.y - 1 < self.height:
			Trail.gotoxy(self.x, self.y - 1)
			print(" ")

	def update(self):
		self.y += 1
		self.list.insert(0, Trail.get_random_char())
		self.list.pop(-1)
		if self.y - self.list_length > self.height:
			self.__init__(self.width, self.height, self.x, 1)

	def get_char_list(self):
		return [Trail.get_random_char() for i in range(0, random.randint(int(self.height * 0.2), int(self.height * 0.4)))]

	@staticmethod
	def get_random_char():
		options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		return random.choice(options)

	@staticmethod
	def gotoxy(x, y):
		sys.stdout.write(f"\033[{y};{x}H")
		sys.stdout.flush()
