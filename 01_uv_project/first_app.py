import httpx
from colorama import Fore


def main():
    print('-' * 60)
    print('Talk Python title finder')
    print('-' * 60)

    num = get_number()
    title = get_title(num)

    print(f'The title for episode {Fore.GREEN}{num} is {Fore.YELLOW}{title}')

    numbers = [1, 2, 5]
    for i, number in enumerate(numbers):
        print(f"The index is {i}, the number is {number} and the title is {get_title(number)}")


def get_number():
    return int(input("Enter the number of the episode: "))


def get_title(episode_number: int) -> str:
    """
    Fetches the title of a given episode from the TalkPython.fm website using the episode number.

    This function sends an HTTP request to fetch the title of the specified episode.
    It constructs the request URL using the provided episode number, fetches the
    response, and then returns the title.

    Args:
        episode_number: The number representing the episode for which the title
            needs to be fetched.

    Returns:
        str: The title of the episode as a string.

    Raises:
        httpx.RequestError: If there is an issue with the HTTP request.
        httpx.HTTPStatusError: If the HTTP response contains an unsuccessful status code.
    """
    # https://talkpython.fm/episodes/show/492/great-tables.title
    url = f'https://talkpython.fm/episodes/show/{episode_number}/any-text-here.title'

    resp = httpx.get(url)
    resp.raise_for_status()

    return resp.text.strip()


if __name__ == '__main__':
    main()
