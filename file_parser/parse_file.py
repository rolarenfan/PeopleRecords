#!/usr/bin/env python
import argparse

import os
import sys

from model.person import (Person, sort_by_birthdate, sort_by_gender, sort_by_lastname)

def parse_line(line):
    """
        Parse one line of the input file, or the one line sent on the POST.

        :param line: string
        :return: [] of string
    """
    if not line:
        return []

    line = line.rstrip()  # Remove trailing \n

    splitter = None  # Will be one of { ',' '|' None }
    if ',' in line:
        splitter = ','
    elif '|' in line:
        splitter = '|'

    splits = line.split(splitter) if splitter else line.split()
    return [datum.strip() for datum in splits]


def parse_file():
    # Create our little parser:
    cmd_parser = argparse.ArgumentParser(
        prog='parse_people',
        description='Parse the content of a file, assumed to be '
                    'space-, comma-, or pipe-separated values')

	# Add the one argument, the path to the file:
    cmd_parser.add_argument('Path',
                            metavar='path',
                            type=str,
                            help='the file to parse')
    # cmd_parser.add_argument('-s',
    #                         action='store',
    #                         choices=['gender', 'birthdate', 'lastname'],
    #                         help='sorting mode')

    # Parse the command:
    args = cmd_parser.parse_args()

    # sort_mode = args.s

    input_path = args.Path
    lines = []
    people = []

    if not os.path.isfile(input_path):
        print('The file specified was not found.')
    else:
        with open(input_path, 'r') as reader:
            for line in reader.readlines():
                line = parse_line(line)
                people.append(Person(line))

        # TODO(ptk): extract the sorts into functions to be used here and in server.
        print([str(person) for person in sorted(people, key=sort_by_birthdate)], '\n')
        print([str(person) for person in sorted(people, key=sort_by_lastname, reverse=True)], '\n')
        print([str(person) for person in sorted(sorted(people, key=sort_by_lastname), key=sort_by_gender)])


if __name__ == "__main__":
    parse_file()
