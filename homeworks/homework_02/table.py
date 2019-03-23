#!/usr/bin/env python
import sys
from json_decomposer import json_show_as_table
from tsv_decomposer import tsv_show_as_table

# Ваши импорты
if __name__ == '__main__':
    filename = sys.argv[1]
    if not filename:
        print("Файл не валиден")
        exit(-1)
    errflag = 0
try:
    json_show_as_table(filename)
except ValueError:
    errflag = 1
except FileExistsError:
    print("Файл не валиден")
    exit(-1)

if errflag:
    try:
        tsv_show_as_table(filename)
    except FileExistsError:
        print("Файл не валиден")
        exit(-1)
    except ValueError:
        print("Формат не валиден")
        exit(-2)
