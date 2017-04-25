#!/usr/bin/python

import unicodedata
import TestCollection


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode("utf-8")

if __name__ == '__main__':
    test_tracker = TestCollection.TestCollection()
    test_tracker.load()

    for title, section in test_tracker:
        print("Inizio sezione " + title)
        camel_code_title = remove_accents(title.title().replace(" ", "") + ".tex")
        section_file = open(camel_code_title, 'w')
        section_file.write("\\begin{center}\n")
        section_file.write("\t\\begin{longtable}{|c|>{\centering}m{10cm}|c|}\\hline\n")
        section_file.write("\t\tId & Descrizione & stato \\\\ \\hline\n")
        for id, test in section:
            implemented_tex = 'Non implementato'
            if test['implemented']:
                implemented_tex = 'Implementato'
            section_file.write("\t\t" + id + " & " + test['description'] + " & " + implemented_tex + " \\\\ \\hline\n")
        section_file.write("\t\\end{longtable}\n")
        section_file.write("\\end{center}\n")
        section_file.close()
