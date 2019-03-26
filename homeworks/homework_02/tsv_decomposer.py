#!/usr/bin/env python
import csv
from file_opener import detect_and_open
from table_printer import tabulate


def _open_and_decompose(filepath):
    fd = detect_and_open(filepath)
    line_of_lines = []
    rows = []
    if fd is None:
        raise FileExistsError
    rd = csv.reader(fd, delimiter='\t')
    for row in rd:
        if len(row) == 0:
            raise ValueError
        rows.append(row)
    for i in range(0, len(rows)):
        if len(rows[i]) != len(rows[0]):
            return ValueError
    for i in range(0, len(rows)):
        if len(rows[i]) == 0:
            raise ValueError
        for k in range(0, len(rows[i])):
            if type(rows[i][k]) != str:
                raise ValueError
            if not rows[i][k]:
                raise ValueError
            if i == 0:
                temp = []
                temp.append(rows[i][k])
                line_of_lines.append(temp)
            else:
                try:
                    line_of_lines[k].append(rows[i][k])
                except IndexError:
                    raise ValueError
    for i in range(0, len(line_of_lines)):
        if len(line_of_lines[i]) != len(line_of_lines[0]):
            raise ValueError
    fd.close()
    return line_of_lines


def tsv_show_as_table(filepath):
    lls = _open_and_decompose(filepath)
    tabulate(lls)
