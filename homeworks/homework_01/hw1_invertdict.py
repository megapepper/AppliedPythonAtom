#!/usr/bin/env python
# coding: utf-8

def func(d_val, result_dict, k):
    if type(d_val) != list and type(d_val) != set and type(d_val) != tuple:
        if result_dict.get(d_val) is None:
            result_dict[d_val] = k
        elif type(result_dict.get(d_val)) != list and type(
                result_dict.get(d_val)) != set and type(
            result_dict.get(d_val)) != tuple:
            result_dict[d_val] = [result_dict.get(d_val), k]
        else:
            result_dict.get(d_val).append(k)
    else:
        for element in d_val:
            func(element, result_dict, k)

def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    out_dict = {}
    if source_dict:
        for k in source_dict.keys():
            func(source_dict.get(k), out_dict, k)
        return out_dict
    else:
        return out_dict
