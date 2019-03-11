#!/usr/bin/env python
# coding: utf-8

def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        sum = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            sum += mul * determinant(m, sign * matrix[0][i])
        return sum

def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    if list_of_lists == [[]] or len(list_of_lists) != len(list_of_lists[0]):
        return None
    else:
        return determinant(list_of_lists, 1)
