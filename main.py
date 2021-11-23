#! /usr/bin/env python3
import os
import random
import cursor
from Trail import Trail

def main():
    try:
        cursor.hide()
        os.system('clear')
        width, height = os.get_terminal_size()
        trails = [Trail(width, height, x, random.randrange(1, height)) for x in range(1, width + 1)]
        while True:
            for trail in trails:
                trail.draw()
                trail.update()
        Trail.gotoxy(1, height-1)
    except KeyboardInterrupt:
        os.system('clear')
        cursor.show()

if __name__ == '__main__':
    main()
