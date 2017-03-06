#!/usr/bin/python

import sys
import json
import codecs
from collections import OrderedDict
import os

req_file = "requirements.json"


def load_requirements():
    # Check if file exists
    if not os.path.exists(req_file):
        file = open(req_file, 'w')
        file.write('{}')
        file.close()
    # Open and parse the file
    req = {}
    with codecs.open(req_file, 'r', "utf-8") as data_file:
        try:
            # Load the json file to the ram.
            req = json.load(data_file, object_pairs_hook=OrderedDict)
        except json.decoder.JSONDecodeError:
            # Shit happens
            print('Errore di sintassi nel file: ' + req_file)
    return req


def print_table(name, column1, column2, data):
    section_file = open(name + ".tex", 'w')
    section_file.write("\\begin{center}\n")
    section_file.write("\t\\begin{longtable}{|p{7cm}|p{5cm}|}\\hline\n")
    section_file.write("\t\t" + column1 + " & " + column2 + " \\\\ \\hline\n")
    for row in data:
        section_file.write("\t\t" + row + " & ")
        for item in data[row]:
            section_file.write(item + " \\\\ & ")
        section_file.write("\\\\ \\hline\n")
    section_file.write("\t\\end{longtable}\n")
    section_file.write("\\end{center}\n")
    section_file.close()


def main(args, argc):
    req = load_requirements()

    class_req = {}
    req_class = {}
    req_package = {}
    package_req = {}

    for packages in req:
        print("Analizzo il package: " + packages)
        sub_puckage = packages.split(".")
        for package in sub_puckage:
            if package not in package_req:
                package_req[package] = []
            for classe in req[packages]:
                print("Analizzo la classe: " + classe)
                if classe not in class_req:
                    class_req[classe] = []
                for requiremt in req[packages][classe]["requisiti"]:
                    if requiremt not in req_class:
                        req_class[requiremt] = []
                        req_package[requiremt] = []

                    if requiremt not in package_req[package]:
                        package_req[package].append(requiremt)
                    if package not in req_package[requiremt]:
                        req_package[requiremt].append(package)
                    if requiremt not in class_req[classe]:
                        class_req[classe].append(requiremt)
                    if classe not in req_class[requiremt]:
                        req_class[requiremt].append(classe)

        print(package_req)
        print(req_package)
        print(class_req)
        print(req_class)
        print_table("PackageReq", "Package", "Id Requisiti", package_req)
        print_table("ReqPackage", "Id Requisiti", "Package", req_package)
        print_table("ClasseReq", "Classe", "Id Requisiti", class_req)
        print_table("ReqClasse", "Id Requisiti", "Classe", req_class)

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))