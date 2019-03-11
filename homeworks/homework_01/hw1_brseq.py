#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    a = input_string
    while len(a) > 0:
        input_string = input_string.replace('()', '')
        input_string = input_string.replace('[]', '')
        input_string = input_string.replace('{}', '')
        if a == input_string:
            break
        a = input_string
    if len(a) == 0:
        return True
    else:
        return False
