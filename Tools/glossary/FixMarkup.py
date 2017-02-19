#!/usr/bin/python

# This script will search through the file if a word present in the glossary is not market correctly
# correcting the markup.

import re
import sys
import Glossary
import glob
from shutil import move
from os import remove
import IgnoreUtils

NOT_REGEX = '\s(?!termine\{)__WORD__(?!\})\s'
REG_EX = 'termine\{([^\}]+)\}+'


def fix_line(string, glossary):
    """
    Corrects the markup of the provided string an returns the fixed one.
    :param string: String that will be fixed.
    :param glossary: Glossary instance that hold all the words.
    :return: string with the correct markup.
    """
    # Search all the marked words
    founded_words = re.findall(REG_EX, string, re.IGNORECASE)
    for word in founded_words:
        # Check if the current word is present in the glossary
        if not glossary.is_present(word):
            # Removes the markup from the string
            string = string.replace("\\termine{" + word + "}", word)
            print(string)
            print("Removed markup to: " + word)

    for title, section in glossary:
        for word, description in section:
            # Replace all the words that should have the markup
            string = re.sub(
                # Prepare the search regex
                NOT_REGEX.replace('__WORD__', word),
                # String that will be replaced all the matches
                " \\\\termine{" + word + '} ',
                string
            )
    return string


def fix_file(file_path, glossary):
    """
    Corrects the markup of the provided file.
    :param file_path: path of the file that will be fixed.
    :param glossary: Glossary instance that hold all the words.
    """
    # Create a temporary backup of the old file
    move(file_path, file_path + '.back')
    # Open and recreate an empty file with the original name
    with open(file_path, 'w') as new_file:
        # Open the old file
        with open(file_path + '.back') as old_file:
            # Iterate over all the old file lines
            for line in old_file:
                # Write to the new file the fixed lines
                new_file.write(fix_line(line, glossary))
    # Delete the old file
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

    ignore_list = IgnoreUtils.load_ignore_list()

    # Iterate over the file and do the parsing
    for filename in glob.iglob(result, recursive=True):
        if IgnoreUtils.ignore_file(ignore_list, filename):
            print('Ignored: ' + filename)
        else:
            print('Parsing: ' + filename)
            fix_file(filename, glossary)


if __name__ == '__main__':
    main(sys.argv)
