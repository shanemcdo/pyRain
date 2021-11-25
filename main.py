#! /usr/bin/env python3
import os
import random
import cursor
import time
from Trail import Trail

def main():
    desired_time = 0.05
    try:
        cursor.hide()
        os.system('clear')
        width, height = os.get_terminal_size()
        trails = [Trail(width, height, x, random.randrange(-30, height)) for x in range(1, width + 1)]
        while True:
            start_time = time.perf_counter()
            for trail in trails:
                trail.draw()
                trail.update()
            elapsed_time = time.perf_counter() - start_time
            remaining_time = desired_time - elapsed_time
            if remaining_time > 0:
                time.sleep(remaining_time)
        Trail.gotoxy(1, height-1)
    except KeyboardInterrupt:
        os.system('clear')
        cursor.show()

if __name__ == '__main__':
    main()
