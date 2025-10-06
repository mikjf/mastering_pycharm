import httpx
from colorama import Fore


def main():
    print('-' * 60)
    print('Talk Python title finder')
    print('-' * 60)

    num = get_number()
    title = get_title(num)

    print(f'The title for episode {Fore.GREEN}{num} is {Fore.YELLOW}{title}')


def get_number():
    return int(input("Enter the number of the episode: "))


def get_title(episode_number: int) -> str:
    # https://talkpython.fm/episodes/show/492/great-tables.title
    url = f'https://talkpython.fm/episodes/show/{episode_number}/any-text-here.title'

    resp = httpx.get(url)
    resp.raise_for_status()

    return resp.text.strip()


if __name__ == '__main__':
    main()
