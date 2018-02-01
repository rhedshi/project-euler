#!/usr/bin/env python3

import os
import textwrap
from typing import ClassVar, List, Tuple

from bs4 import BeautifulSoup
import click
import requests


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
        Returns the string representation of this problem.
        """
        title = f'Problem {self.number} - {self.title}'
        underline = '=' * len(title)
        description = '\n\n'.join([
            textwrap.fill(s, 80)
            for s in self.description
        ])

        return f'{title}\n{underline}\n\n{description}'


class ProjectEuler():
    """
    Class for querying and downloading problems from the Project Euler website.
    """

    PROBLEMS_DIR: ClassVar[str] = './problems'

    @staticmethod
    def get_last_id() -> int:
        """
        Returns the most recent problem number on the website.
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

    @staticmethod
    def get_problem(number: int) -> Problem:
        """
        Returns the problem scraped from the website.
        """
        url = f'https://projecteuler.net/problem={number}'
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

    @staticmethod
    def write_problem(problem: Problem, file_path: str) -> None:
        """
        Writes the problem to the given file path.
        """
        with open(file_path, 'w') as f:
            f.write('#!/usr/bin/env python3\n')
            f.write('# -*- coding: utf-8 -*-\n')
            f.write('\n"""\n')
            f.write(str(problem))
            f.write('\n"""\n')

    @classmethod
    def download_problems(cls,
                          start: int, end: int,
                          dir: str, overwrite: bool=False) -> None:
        """
        Downloads a range of problems (inclusive) from the website to the
        given directory.
        """
        if not os.path.exists(dir):
            raise Exception(f'The \'{dir}\' directory does not exist.')

        if not os.path.isdir(dir):
            raise Exception(f'\'{dir}\' is not a directory.')

        for i in range(start, end + 1):
            file_path = os.path.join(dir, f'{i:03}_problem.py')

            # WARNING: Do not overwrite existing file
            if not overwrite and os.path.exists(file_path):
                continue

            problem = cls.get_problem(i)
            cls.write_problem(problem, file_path)


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--all',
    is_flag=True,
    default=False,
    help='Download all the problems.',
)
@click.option(
    '--tail',
    nargs=1,
    type=int,
    metavar='N',
    help='Download the last N problems.',
)
@click.option(
    '--overwrite',
    is_flag=True,
    default=False,
    help='Overwrite any existing problem files.',
)
@click.argument(
    'problems',
    nargs=-1,
    type=str,
)
def download(all: bool, tail: int,
             overwrite: bool, problems: Tuple[str]) -> None:
    """
    Download Project Euler problems from the website.

    [PROBLEMS] - List of problem number ranges (ex. '1-5 10 20-25')
    """
    path = ProjectEuler.PROBLEMS_DIR

    if not os.path.exists(path):
        if click.confirm(f'Create the {path} directory?'):
            os.mkdir(path)

    if overwrite:
        overwrite = click.confirm('Overwrite existing problem files?')

    last = ProjectEuler.get_last_id()

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

        ProjectEuler.download_problems(start, end, path, overwrite)


if __name__ == "__main__":
    cli()
