import asyncio
from asyncio import AbstractEventLoop

import aiohttp
import bs4
from colorama import Fore


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range(loop))
    print('done')


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f'get HTML for episode {episode_number}', flush=True)

    url = f'https://talkpython.fm/{episode_number}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f'get title for episode {episode_number}', flush=True)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return 'missing'

    return header.text.strip()


async def get_title_range(loop: AbstractEventLoop):
    tasks = [(loop.create_task(get_html(n)), n) for n in range(195, 200)]

    for task, episode_number in tasks:
        html = await task
        title = get_title(html, episode_number)
        print(Fore.WHITE + f'title found: {title}', flush=True)


if __name__ == '__main__':
    main()
