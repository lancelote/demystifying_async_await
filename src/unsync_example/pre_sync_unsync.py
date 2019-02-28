import asyncio
import datetime as dt
import math
import aiohttp
import requests


async def compute_some():
    print('computing...')
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


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


async def download_some_more():
    print('downloading...')
    url = 'https://pythonbytes.fm/episodes/show/92/' \
          'will-your-python-be-compiled'
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    print(f'downloaded {len(text)} characters')


async def wait_some():
    print('waiting...')
    for _ in range(1, 1000):
        await asyncio.sleep(.001)


def main():
    t0 = dt.datetime.now()
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(compute_some()),
        loop.create_task(compute_some()),
        loop.create_task(download_some()),
        loop.create_task(download_some()),
        loop.create_task(download_some_more()),
        loop.create_task(download_some_more()),
        loop.create_task(wait_some()),
        loop.create_task(wait_some()),
        loop.create_task(wait_some()),
        loop.create_task(wait_some()),
    ]

    loop.run_until_complete(asyncio.gather(*tasks))

    d0 = dt.datetime.now() - t0
    print(f'pre async version done in {d0.total_seconds():.2f}s')


if __name__ == '__main__':
    main()
