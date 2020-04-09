import os
import time
import cursor
from Trail import Trail
from msvcrt import kbhit, getch

def kbin():
	global running
	if kbhit():
		ch = getch().decode('utf-8')
		if ch == 'q':
			running = False
			 

def main():
	global running
	cursor.hide()
	os.system("cls")
	width, height = os.get_terminal_size()
	trail = Trail(width, height, 20,10)
	running = True
	while running:
		trail.draw()
		trail.update()
		kbin()
		time.sleep(0.01)
	Trail.gotoxy(1,height-1)
	cursor.show()

if __name__ == '__main__':
	main()
