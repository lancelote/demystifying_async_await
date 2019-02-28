import requests
import bs4
from colorama import Fore


def main():
    get_title_range()
    print('done')


def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f'get HTML for episode {episode_number}', flush=True)

    url = f'https://talkpython.fm/{episode_number}'
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f'get title for episode {episode_number}', flush=True)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return 'missing'

    return header.text.strip()


def get_title_range():
    for episode_number in range(195, 200):
        html = get_html(episode_number)
        title = get_title(html, episode_number)
        print(Fore.WHITE + f'title found: {title}', flush=True)


if __name__ == '__main__':
    main()
