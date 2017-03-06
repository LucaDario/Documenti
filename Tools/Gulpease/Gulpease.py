#!/usr/bin/python

import glob
import sys


def gulpease(frasi, parole, lettere):
    lp = (100.0 * lettere) / parole
    fr = (100.0 * frasi) / parole
    result = 89.0 - (lp / 10.0) + (3.0 * fr)
    return int(result)


def gulpease_dir(path):
    # Fix the path
    if path[-1:] != '/':
        path += '/'
    # Prepare the expression used to find the file tath will be parsed
    result = path + '**/*.tex'

    # Iterate over the file and do the parsing
    frasi = 0
    parole = 0
    lettere = 0
    for filename in glob.iglob(result, recursive=True):
        file = open(filename, 'r')
        testo = file.read()
        temp_frasi = testo.count('.') + testo.count('?') + testo.count('!') + testo.count(':') + testo.count(';')
        temp_parole = len(testo.split())
        temp_lettere = len(testo) - temp_parole
        frasi += temp_frasi
        parole += temp_parole
        lettere += temp_lettere
        file.close()
    return gulpease(frasi, parole, lettere)


def gulpease_file(path):
    file = open(path, 'r')
    testo = file.read()
    frasi = testo.count('.') + testo.count('?') + testo.count('!') + testo.count(':') + testo.count(';')
    parole = len(testo.split())
    lettere = len(testo) - parole
    file.close()
    return gulpease(frasi, parole, lettere)


def main(args, argc):
    if argc <= 1:
        print("Inserire il nome della cartella in cui si vuole calcolare l'indice di gulpease")
        return -1

    gulpease_index = -1

    # Fix the path
    if '.tex' in args[1]:
        gulpease_index = gulpease_file(args[1])
    else:
        gulpease_index = gulpease_dir(args[1])

    print("Indice di gulpease per " + args[1] + " = " + str(gulpease_index))


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
