import asyncio
import datetime as dt
import random

import colorama


def main():
    loop = asyncio.get_event_loop()

    t0 = dt.datetime.now()
    print(colorama.Fore.WHITE + 'app started', flush=True)

    data = asyncio.Queue()
    task = asyncio.gather(
        generate_data(10, data),
        generate_data(10, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data),
    )

    loop.run_until_complete(task)

    t1 = dt.datetime.now() - t0
    msg = f'app exiting, total time: {t1.total_seconds():.2f} sec'
    print(colorama.Fore.WHITE + msg)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx * idx
        work = (item, dt.datetime.now())
        await data.put(work)

        msg = f' --- generate item {idx}'
        print(colorama.Fore.YELLOW + msg, flush=True)

        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        item = await data.get()

        processed += 1
        value = item[0]
        t0 = item[1]
        t1 = dt.datetime.now() - t0

        msg = f' +++ process value {value} after {t1.total_seconds():.2f} sec'
        print(colorama.Fore.CYAN + msg, flush=True)
        await asyncio.sleep(.5)


if __name__ == '__main__':
    main()
