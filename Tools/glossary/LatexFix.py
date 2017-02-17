#!/usr/bin/python

import re
import sys
import Glossary
import glob
import os.path
import ntpath
from shutil import move
from os import remove

NOT_REGEX = '\s(?!termine\{)__WORD__(?!\})\s'
IGNORE_FILE = 'glossario.ignore'


def load_ignore_list():
    ignore_list = []
    if os.path.exists(IGNORE_FILE):
        with open(IGNORE_FILE, 'r') as ignore_file:
            for line in ignore_file:
                if not line[0] == '#':
                    ignore_list.append(line.replace('\n', ''))
    return ignore_list


def ignore_file(ignore_list, file_path):
    file_name = ntpath.basename(file_path)
    for ignore_f in ignore_list:
        if re.match(ignore_f, file_name) is not None:
            return True
    return False


def fix_line(line, glossary):
    for title, section in glossary:
        for word, description in section:
            line = re.sub(NOT_REGEX.replace('__WORD__', word), " \\\\termine{" + word + '} ', line)
    return line


def fix_file(file_path, glossary):
    move(file_path, file_path + '.back')
    with open(file_path, 'w') as new_file:
        with open(file_path + '.back') as old_file:
            for line in old_file:
                new_file.write(fix_line(line, glossary))
    remove(file_path + '.back')


def main(args):
    if len(args) <= 1:
        print('Inserire il path della directory che si vuole analizzare')
        sys.exit(1)

    glossary = Glossary.Glossary()
    if not glossary.init():
        sys.exit(1)
    # Fix the path
    if args[1][-1:] != '/':
        args[1] += '/'
    # Prepare the expression used to find the file tath will be parsed
    result = args[1] + '**/*.tex'

    ignore_list = load_ignore_list()

    # Iterate over the file and do the parsing
    for filename in glob.iglob(result, recursive=True):
        if ignore_file(ignore_list, filename):
            print('Ignored: ' + filename)
        else:
            #print('Parsing: ' + filename)
            fix_file(filename, glossary)


if __name__ == '__main__':
    main(sys.argv)
