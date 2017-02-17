import json
import os.path
from collections import OrderedDict
import codecs


# Class to iterate over the words of a glossary section
class WordsIterator:
    # Section of the glossary
    glossary_section = {}
    # Words of the current section
    words = []
    # Counter for the iteration
    current = 0

    def __init__(self, glossary_section):
        self.glossary_section = glossary_section
        self.words = list(glossary_section.keys())

    # Iterator logic
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.words):
            raise StopIteration
        else:
            word = self.words[self.current]
            description = self.glossary_section[word]
            self.current += 1
            return word, description


# Class to iterate over the section of the glossary
class SectionsIterator:
    # Representation of the glossary in ram
    glossary = {}
    # Section of the glossary
    sections = []
    # Counter used in the iteration
    current = 0

    def __init__(self, glossary):
        self.glossary = glossary
        self.sections = list(glossary.keys())
        self.current = 0

    # Iteration logic
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.sections):
            raise StopIteration
        else:
            letter = self.sections[self.current]
            self.current += 1
            return self.sections[self.current - 1], WordsIterator(self.glossary[letter])


# Object used to access the glossary
class Glossary:
    # Glossary file used to save the state to the disk.
    glossary_file = 'glossario.json'

    # Dictionary that hold the value in ram.
    words = {}

    # Initialize the glossary file.
    # Returns False if the file 'glossary_file' is corrupted
    # True otherwise.
    def init(self):
        ok = False
        # Check if file exists
        if not os.path.exists(self.glossary_file):
            file = open(self.glossary_file, 'w')
            file.write('{}')
            file.close()
        # Open and parse the file
        with codecs.open(self.glossary_file, 'r', "utf-8") as data_file:
            try:
                # Load the json file to the ram.
                self.words = json.load(data_file, object_pairs_hook=OrderedDict)
                ok = True
            except json.decoder.JSONDecodeError:
                # Shit happens
                print('Errore di sintassi nel file: ' + self.glossary_file)

        return ok

    # Check if a word is present in the glossary
    def is_present(self, value):
        # Make the first letter uppercase
        value = value.lower().title()
        # Get the fist letter
        first_letter = value[0]
        # Make the check ;)
        return first_letter in self.words and value in self.words[first_letter]

    # Insert a value in the glossary.
    def insert(self, value):
        # Make the first letter uppercase
        value = value.lower().title()
        # Get the fist letter
        first_letter = value[0]
        # Check if the section for the current letter exist
        if first_letter not in self.words:
            # If not initialize a glossary section for this letter
            self.words[first_letter] = {}
        # Insert the word in the glossary
        self.words[first_letter][value] = ''

    # Save the glossary to disk
    def commit(self):
        # Open the file
        file = codecs.open(self.glossary_file, 'w', "utf-8")
        # Pretty print to file.
        file.write(json.dumps(self.words, sort_keys=True, indent=4, separators=(',', ': '),  ensure_ascii=False))
        # Release the resource
        file.close()

    def __iter__(self):
        return SectionsIterator(self.words)
