#! /usr/bin/env python3
import os
import sys
import random
import cursor
import time
from Trail import Trail
from typing import List

def make_trails(width: int, height: int) -> List[Trail]:
    height += 2
    return [Trail(width, height, x, random.randrange(-30, height)) for x in range(1, width + 1)]

def main():
    desired_time = 0.05
    try:
        cursor.hide()
        if sys.platform in ('linux', 'linux2'):
            print('\033[48;2;0;0;0m')
        os.system('clear')
        prev_size =  os.get_terminal_size()
        trails = make_trails(*prev_size)
        while True:
            if (size := os.get_terminal_size()) != prev_size:
                os.system('clear')
                trails = make_trails(*size)
                prev_size = size
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
