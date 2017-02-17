#!/usr/bin/python

# Questo sript ha il compito di parsare i file latex per estrarre i vocaboli che dovranno andare nel glossario
# Genererà file json in output diviso per sezioni nel quale per ogni parola sarà possibile definire la rispettiva descrizione.


import re
import sys
import Glossary
import glob

# NOTA: le parole dovranno rispettare la seguente espressione regolare per essere cosiderate!!
REG_EX = 'termine\{([^\}]+)\}+'


def parse_file(file_path, glossary):
    founded_words = []
    with open(file_path) as FileObj:
        # Iterate over the lines
        for line in FileObj:
            if line[0] != '%':
                # Parse the words in the current line
                words_in_line = re.findall(REG_EX, line)

                # Iterate over all the words founded in the current line
                for word in words_in_line:
                    # If not in the glossary add it
                    if not glossary.is_present(word):
                        print(word)
                        glossary.insert(word)
                        founded_words.append(word)
    return founded_words


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

    founded_words = []

    # Iterate over the file and do the parsing
    for filename in glob.iglob(result, recursive=True):
        print('Parsing: ' + filename)
        founded_words += parse_file(filename, glossary)

    # Save the glossary
    glossary.commit()

    print("Ci sono: " + str(len(founded_words)) + " nuovi termini")
    print(founded_words)

if __name__ == '__main__':
    main(sys.argv)
