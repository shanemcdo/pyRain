import os
from Trail import Trail



def main():
	width, height = os.get_terminal_size()
	trail = Trail(10,5)
	trail.draw()

if __name__ == '__main__':
	main()
