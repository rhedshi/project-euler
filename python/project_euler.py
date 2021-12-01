#!/usr/bin/env python3

import logging
import os
import textwrap
from typing import List, Tuple

from bs4 import BeautifulSoup
import click
import requests

from constants import ROOT_DIR

logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


PROBLEMS_DIR = os.path.join(ROOT_DIR, 'problems')


@click.group(
    context_settings={
        'help_option_names': ['-h', '--help'],
    },
)
def cli():
    pass


@cli.command()
@click.option(
    '--all',
    help='Download all the problems.',
    is_flag=True,
)
@click.option(
    '--tail',
    help='Download the last N problems.',
    metavar='N',
    nargs=1,
    type=int,
)
@click.option(
    '--overwrite',
    help='Overwrite any existing problem files.',
    is_flag=True,
)
@click.argument(
    'problems',
    nargs=-1,
    type=str,
)
def download(
    all: bool,
    tail: int,
    overwrite: bool,
    problems: Tuple[str],
) -> None:
    """
    Download Project Euler problems from the website.

    [PROBLEMS] - List of problem number ranges (ex. '1-5 10 20-25')
    """
    path = PROBLEMS_DIR

    if not os.path.exists(path):
        if click.confirm(f'Create the {path} directory?'):
            os.mkdir(path)

    if overwrite:
        overwrite = click.confirm('Overwrite existing problem files?')

    last = get_last_id()

    if all:
        problems = (f'1-{last}',)
    if tail:
        problems = (f'{last - tail + 1}-{last}',)

    for group in problems:
        try:
            start, end = (
                int(num)
                for num in group.split('-')
            )
        except ValueError:
            start, end = int(group), int(group)

        download_problems(start, end, path, overwrite)


class Problem():
    """
    Represents a Project Euler problem.
    """

    number: int
    title: str
    description: List[str]

    def __init__(self, number: int, title: str, description: List[str]) -> None:
        self.number = number
        self.title = title
        self.description = description

    def __str__(self) -> str:
        """
        Return the string representation of this problem.
        """
        title = f'Problem {self.number} - {self.title}'
        underline = '=' * len(title)
        description = '\n\n'.join([
            textwrap.fill(s, 80)
            for s in self.description
        ])

        return f'{title}\n{underline}\n\n{description}'


def get_last_id() -> int:
    """
    Return the most recent problem number on the website.
    """
    url = 'https://projecteuler.net/recent'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    last_id = soup \
        .find('table') \
        .find_all('tr')[1] \
        .find_all('td')[0] \
        .get_text()

    return int(last_id)


def get_problem(number: int) -> Problem:
    """
    Return the problem number scraped from the website.
    """
    url = f'https://projecteuler.net/problem={number}'

    logger.info(f'Getting {number:03} from {url}')

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h2').get_text()
    problem_content = soup.find('div', class_='problem_content')

    description = []

    for child in problem_content.children:
        try:
            text = child.get_text()
        except AttributeError:
            continue
        description.append(text)

    return Problem(number, title, description)


def write_problem(problem: Problem, file_path: str) -> None:
    """
    Write the problem to the given file path.
    """
    logger.info(f'Writing {problem.number:03} to {file_path}')

    with open(file_path, 'w') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('\n"""\n')
        f.write(str(problem))
        f.write('\n"""\n')


def download_problems(
    start: int,
    end: int,
    dir: str,
    overwrite: bool = False,
) -> None:
    """
    Download range of problems (inclusive) from the website to the
    given directory.
    """
    if not os.path.exists(dir):
        raise Exception(f'The \'{dir}\' directory does not exist.')

    if not os.path.isdir(dir):
        raise Exception(f'\'{dir}\' is not a directory.')

    for i in range(start, end + 1):
        file_name = f'{i:03}_problem.py'
        file_path = os.path.join(dir, file_name)

        # WARNING: Do not overwrite existing file
        if os.path.exists(file_path) and not overwrite:
            logger.info(f'...Skipping {i:03}')
            continue

        problem = get_problem(i)
        write_problem(problem, file_path)


if __name__ == '__main__':
    cli()
