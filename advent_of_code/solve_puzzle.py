import os
from importlib import import_module
from time import perf_counter

import click


def read_file(filename: str) -> str:
    with open(filename, mode='r') as f:
        return f.read()


def format_duration(secs: float) -> str:
    if secs < 1:
        return f'{secs * 1000:.3f}ms'
    else:
        return f'{secs:.2f}s'


def run_puzzle(year: int, day: int, part: int):
    # load puzzle input file
    input_txt_filename = os.path.join(
        os.path.dirname(__name__),
        'advent_of_code',
        f'year{year}',
        f'day{day:02d}',
        'input.txt',
    )
    try:
        input_txt = read_file(input_txt_filename).strip()
    except FileNotFoundError:
        print(f'\nError: Could not find puzzle input for {year}, day{day}, part{part}')
        return

    try:
        module = import_module(f'advent_of_code.year{year}.day{day:02d}.part{part}')
    except ImportError:
        print(f'\nError: Could not find puzzle solution for {year}, day{day}, part{part}')
        return

    if not hasattr(module, 'main'):
        print(f'\nError: Could not find "main" method for puzzle {year}, day{day}, part{part}')
        return

    t0 = perf_counter()
    result = module.main(input_txt)
    t1 = perf_counter()

    print(f'\nPuzzle: {year}, day{day}, part{part}')
    print(f'Result: {result}')
    print(f'Time  : {format_duration(t1 - t0)}')


@click.command()
@click.option('--year', type=int, default=2022)
@click.option('--day', type=int, required=True)
@click.option('--part', type=int, default=None)
def main(year: int, day: int, part: int):
    if part is None:
        run_puzzle(year, day, part=1)
        run_puzzle(year, day, part=2)
    else:
        run_puzzle(year, day, part=part)


if __name__ == '__main__':
    main()
