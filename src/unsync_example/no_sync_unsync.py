import datetime as dt
import math
import time
import requests


def compute_some():
    print('computing...')
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


def download_some():
    print('downloading...')
    url = 'https://talkpython.fm/episodes/show/174/' \
          'coming-into-python-from-another-industry-part-2'
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    print(f'downloaded {len(text)} characters')


def download_some_more():
    print('downloading...')
    url = 'https://pythonbytes.fm/episodes/show/92/' \
          'will-your-python-be-compiled'
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    print(f'downloaded {len(text)} characters')


def wait_some():
    print('waiting...')
    for _ in range(1, 1000):
        time.sleep(.001)


def main():
    t0 = dt.datetime.now()

    compute_some()
    compute_some()
    compute_some()

    download_some()
    download_some()

    download_some_more()
    download_some_more()

    wait_some()
    wait_some()
    wait_some()
    wait_some()

    d0 = dt.datetime.now() - t0
    print(f'sync version done in {d0.total_seconds():.2f}s')


if __name__ == '__main__':
    main()
