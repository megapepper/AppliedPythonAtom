#!/usr/bin/env python
import json
from file_opener import detect_and_open
from table_printer import tabulate


def _open_and_decompose(filepath):
    line_of_lines = []
    fd = detect_and_open(filepath)
    if fd is None:
        raise FileExistsError
    try:
        struct = json.load(fd)
    except json.JSONDecodeError:
        raise ValueError
    for i in range(0, len(struct)):
        if len(struct[i]) != len(struct[0]):
            return ValueError
    for i in range(0, len(struct)):
        k_ind = 0
        for k in struct[i].keys():
            if not (struct[i])[k]:
                raise ValueError
            if i == 0:
                temp = []
                temp.append(k)
                temp.append(str((struct[i])[k]))
                line_of_lines.append(temp)
            else:
                try:
                    line_of_lines[k_ind].append(str((struct[i])[k]))
                except IndexError:
                    raise ValueError
            k_ind = k_ind + 1
    for i in range(0, len(line_of_lines)):
        if len(line_of_lines[i]) != len(line_of_lines[0]):
            raise ValueError
    fd.close()
    return line_of_lines


def json_show_as_table(filepath):
    lls = _open_and_decompose(filepath)
    tabulate(lls)
