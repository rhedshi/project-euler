#!/usr/bin/env python

'''
Command-line script for downloading problems from the website.

Usage: ./project_euler.py [-h] {all, problem, range, last} ...

Main commands:
    all         downloads all the problems
    problem     downloads single problem
    range       downloads range of problems (inclusive)
    last        downloads last n problems
'''

import argparse
import os
import textwrap

from lxml import html
import requests

class Problem(object):
    '''
    Project Euler Problem
    '''
    def __init__(self, number, title, description):
        self.number = number            # Number
        self.title = title              # String
        self.description = description  # Array of strings

    def generate_full_text_description(self):
        '''
        Generates a formatted full text description of the problem
        '''
        title = 'Problem ' + str(self.number) + ' - ' + self.title
        underline = len(title) * '='
        description = '\n'.join([textwrap.fill(s.encode('utf-8'), 80) for s in self.description])
        return title + '\n' + underline + '\n' + description

def main():
    args = parse_args()
    # Creates a Problems folder if there isn't one
    if not os.path.exists('./problems'):
        os.mkdir('problems')
    # Get the start and end range for problems
    start, end = get_start_end_range(args)
    for i in xrange(start, end):
        # Check if the problem file already exists
        file_name = 'problem' + str(i) + '.py'
        file_path = './problems/' + file_name
        if os.path.exists(file_path):
            # Do not overwrite if the file already exists
            pass
        else:
            download_problem(i, file_path)
    return

def parse_args():
    '''
    Parse command-line arguments
    '''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    # All problems
    parser_all = subparsers.add_parser('all', help='downloads all problems')
    # Single problem
    parser_single = subparsers.add_parser('problem', help='downloads single problem')
    parser_single.add_argument('problem_number', metavar='n', type=int, help='problem number')
    # Range of problems (inclusive)
    parser_range = subparsers.add_parser('range', help='downloads range of problems (inclusive)')
    parser_range.add_argument('start', type=int, help='problem number')
    parser_range.add_argument('end', type=int, help='problem number')
    # Last n problems
    parser_last = subparsers.add_parser('last', help='downloads last n problems')
    parser_last.add_argument('last', metavar='n', type=int, help='number of problems')
    return parser.parse_args()

def download_problem(number, file_path):
    '''
    Downloads the problem to the given file path as a commented header section
    containing the full problem description.
    '''
    # Get the problem from the website
    problem = get_problem(number)
    # Write the problem description as a commented header in the file
    f = open(file_path, 'w')
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\n' + problem.generate_full_text_description() + '"""\n')
    f.close()
    return

def get_problem(number):
    '''
    Returns a Problem created from its problem page on the website
    '''
    # Parse the problem page on the website for title and description fields
    page = requests.get('https://projecteuler.net/problem=' + str(number))
    tree = html.fromstring(page.text)
    title = tree.xpath('//h2/text()')[0]
    description = tree.xpath('//div[@class="problem_content"]//text()')
    return Problem(number, title, description)

def get_most_recent_problem_number():
    '''
    Returns the most recent problem number on the website
    '''
    # Parse the recent URL for the most recently released problem number
    page = requests.get('https://projecteuler.net/recent')
    tree = html.fromstring(page.text)
    recent_ids = tree.xpath('//table[@id="problems_table"]//tr/td[1]/text()')
    return int(recent_ids[0])

def get_start_end_range(args):
    '''
    Returns the start and end range for downloading problems
    '''
    start = 0
    end = 0
    most_recent = get_most_recent_problem_number()
    if args.command == 'all':
        start = 1
        end = most_recent + 1
    elif args.command == 'problem':
        start = args.problem_number
        end = args.problem_number + 1
    elif args.command == 'range':
        start = args.start
        end = args.end + 1
    elif args.command == 'last':
        start = most_recent - args.last + 1
        end = most_recent + 1
    else:
        pass
    # Ensure start and end stay within allowable range
    start = min(max(start, 1), most_recent + 1)
    end = min(max(end, 1), most_recent + 1)
    if start > end:
        start, end = end, start
    return start, end

if __name__ == "__main__":
    main()
