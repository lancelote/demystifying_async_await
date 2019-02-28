import asyncio
import datetime as dt
import math
import aiohttp
import requests

from unsync import unsync


@unsync(cpu_bound=True)  # will run with multiprocessing
def compute_some():
    print('computing...')
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


@unsync  # will run as usual with asyncio event loop
async def download_some():
    print('downloading...')
    url = 'https://talkpython.fm/episodes/show/174/' \
          'coming-into-python-from-another-industry-part-2'
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
    print(f'downloaded {len(text)} characters')


@unsync  # will run on a thread
def download_some_more():
    print('downloading...')
    url = 'https://pythonbytes.fm/episodes/show/92/' \
          'will-your-python-be-compiled'
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    print(f'downloaded {len(text)} characters')


@unsync  # will run as usual with asyncio event loop
async def wait_some():
    print('waiting...')
    for _ in range(1, 1000):
        await asyncio.sleep(.001)


def main():
    t0 = dt.datetime.now()

    tasks = [
        compute_some(),
        compute_some(),
        download_some(),
        download_some(),
        download_some_more(),
        download_some_more(),
        wait_some(),
        wait_some(),
        wait_some(),
        wait_some(),
    ]

    # waiting for tasks
    for task in tasks:
        task.result()

    d0 = dt.datetime.now() - t0
    print(f'pre async version done in {d0.total_seconds():.2f}s')


if __name__ == '__main__':
    main()
