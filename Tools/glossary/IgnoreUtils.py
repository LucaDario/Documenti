import os.path
import ntpath
import re

IGNORE_FILE = 'glossario.ignore'


def load_ignore_list():
    """
    Loads the list of the files that will be ignored during the process.
    :return: An array representing the files that will be ignored during the process.
    """
    ignore_list = []
    if os.path.exists(IGNORE_FILE):
        with open(IGNORE_FILE, 'r') as ignore_file:
            for line in ignore_file:
                if not line[0] == '#':
                    ignore_list.append(line.replace('\n', ''))
    return ignore_list


def ignore_file(ignore_list, file_path):
    """
    Checks if the file should be ignored.
    :param ignore_list: Array with the list of the file that must be ignored.
    :param file_path: Path of the file to check.
    :return: True if the file must be ignored False otherwise.
    """
    file_name = ntpath.basename(file_path)
    for ignore_f in ignore_list:
        if re.match(ignore_f, file_name) is not None or re.match(ignore_f, file_path):
            return True
    return False