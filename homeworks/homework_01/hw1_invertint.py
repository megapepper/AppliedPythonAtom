#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    s = str(number)
    print(number)
    if number >= 0:
        out = s[::-1]
        out.strip("0")
        print(out)
        return int(out)
    else:
        out = s[::-1].replace('-', '')
        out = '-' + out.strip("0")
        print(out)
        return int(out)
