#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        heap = MaxHeap([])
        output_list = []
        for single_list in list_of_lists:
            for i in single_list:
                heap.add(i)
        for i in range(0, k):
            try:
                max_elem = heap.extract_maximum()
            except IndexError:
                break
            output_list.append(max_elem)
        return output_list
