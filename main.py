import os
import cursor
from Trail import Trail


def main():
	cursor.hide()
	width, height = os.get_terminal_size()
	trail = Trail(10,5)
	trail.draw()
	Trail.gotoxy(1,height-1)
	cursor.show()

if __name__ == '__main__':
	main()
