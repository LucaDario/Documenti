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
        camel_code_results_title = "Esiti" + camel_code_title
        section_file = open(camel_code_title, 'w')
        results_file = open(camel_code_results_title, 'w')

        section_file.write("\\begin{center}\n")
        section_file.write("\t\\begin{longtable}{|c|>{\centering}m{10cm}|c|}\\hline\n")
        section_file.write("\t\tId & Descrizione & Stato\\\\ \\hline\n")

        results_file.write("\\begin{center}\n")
        results_file.write("\t\\begin{longtable}{|c|>{\centering}m{10cm}|c|}\\hline\n")
        results_file.write("\t\tId & Descrizione & Esito\\\\ \\hline\n")

        for id, test in section:
            implemented_tex = '\\textcolor{Orange}{Non implementato}'
            if test['implemented']:
                implemented_tex = '\\textcolor{Green}{Implementato}'
            section_file.write("\t\t" + id + " & " + test['description'] + " & " + implemented_tex + "\\\\ \\hline\n")

            result_text = '\\textcolor{Orange}{Non superato}'
            if test['passed']:
                result_text = '\\textcolor{Green}{Superato}'
            results_file.write("\t\t" + id + " & " + test['description'] + " & " + result_text + "\\\\ \\hline\n")

        section_file.write("\t\\end{longtable}\n")
        section_file.write("\\end{center}\n")
        section_file.close()

        results_file.write("\t\\end{longtable}\n")
        results_file.write("\\end{center}\n")
        results_file.close()
