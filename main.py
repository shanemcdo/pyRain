import os
from Trail import Trail



def main():
	width, height = os.get_terminal_size()
	trail = Trail(1,1)
	print(trail.list)

if __name__ == '__main__':
	main()
