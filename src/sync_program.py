import random
import time
import datetime as dt
from typing import List

import colorama


def main():
    t0 = dt.datetime.now()
    print(colorama.Fore.WHITE + 'app started', flush=True)
    data = []
    generate_data(10, data)
    generate_data(10, data)
    process_data(20, data)

    t1 = dt.datetime.now() - t0
    msg = f'app exiting, total time: {t1.total_seconds():.2f} sec'
    print(colorama.Fore.WHITE + msg)


def generate_data(num: int, data: List):
    for idx in range(1, num + 1):
        item = idx*idx
        data.append((item, dt.datetime.now()))

        msg = f' --- generate item {idx}'
        print(colorama.Fore.YELLOW + msg, flush=True)
        time.sleep(random.random() + .5)


def process_data(num: int, data: List):
    processed = 0
    while processed < num:
        item = data.pop(0)
        if not item:
            time.sleep(.01)
            continue

        processed += 1
        value = item[0]
        t0 = item[1]
        t1 = dt.datetime.now() - t0
        msg = f' +++ process value {value} after {t1.total_seconds():.2f} sec'
        print(colorama.Fore.CYAN + msg, flush=True)
        time.sleep(.5)


if __name__ == '__main__':
    main()
