import os
import re
from datetime import datetime
from time import sleep

import click
import requests
from dotenv import load_dotenv
from markdownify import markdownify as md

load_dotenv()


def fetch_puzzle_input(session_cookie: str, year: int, day: int) -> str:
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session_cookie}
    )
    # https://www.reddit.com/r/adventofcode/comments/3v64sb/aoc_is_fragile_please_be_gentle/
    sleep(1)
    if resp.status_code == 200:
        return resp.text
    else:
        raise Exception(f"Could not fetch puzzle input: {resp.text}")


def fetch_puzzle(session_cookie: str, year: int, day: int) -> str:
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{day}", cookies={"session": session_cookie}
    )
    # https://www.reddit.com/r/adventofcode/comments/3v64sb/aoc_is_fragile_please_be_gentle/
    sleep(1)
    if resp.status_code == 200:
        return resp.text
    else:
        raise Exception(f"Could not fetch puzzle: {resp.text}")


def extract_puzzle_description(puzzle: str) -> str:
    """
    Extracts puzzle description from html.
    There can be two descriptions, one for part 1 and one for part 2.
    """
    RE_PUZZLE_DESC = re.compile(
        r"""\<article class="day-desc"\>(.+?)\<\/article\>""", re.MULTILINE | re.DOTALL
    )
    descriptions = []
    for html in RE_PUZZLE_DESC.findall(puzzle):
        # Convert html to markdown and append to description
        descriptions.append(md(html))
    return "".join(descriptions)


def write_file(contents: str, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf8") as f:
        f.write(contents)


def download_puzzle(session_cookie: str, year: int, day: int):
    path = os.path.join(
        os.path.dirname(__name__),
        'advent_of_code',
        f'year{year}',
        f'day{day:02d}',
    )

    # download input if it doesn't already exist'
    input_path = os.path.join(path, "input.txt")
    if not os.path.exists(input_path):
        puzzle_input = fetch_puzzle_input(session_cookie, year, day)
        write_file(puzzle_input, input_path)
        print(f"Dowloaded input for : {year} day{day}")

    # download puzzle description even if it exists since part 2 unlocks after part 1 is solved
    puzzle_path = os.path.join(path, "puzzle.md")
    puzzle = fetch_puzzle(session_cookie, year, day)
    write_file(extract_puzzle_description(puzzle), os.path.join(path, "puzzle.md"))
    print(f"Dowloaded puzzle for: {year} day{day}")


@click.command()
@click.option("--year", type=int, required=True)
@click.option("--day", type=int, required=False)
def main(year: int, day: int):
    session_cookie: str = os.environ['SESSION_COOKIE']
    now = datetime.now()
    if day is None:
        for day in range(1, 26):
            if year == now.year and day > now.day:
                break
            download_puzzle(session_cookie, year, day)
    else:
        download_puzzle(session_cookie, year, day)

    print("Downloads complete!")


if __name__ == '__main__':
    main()
