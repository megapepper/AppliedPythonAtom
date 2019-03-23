#!/usr/bin/env python
# coding: utf-8

import copy


class Heap():

    def __init__(self, array):
        self.elements = copy.deepcopy(array)
        self.build_heap()

    def add(self, elem_with_priority):
        self.elements.append(copy.deepcopy(elem_with_priority))
        self.build_heap()

    def build_heap(self):
        print(self.elements)
        if len(self.elements) > 0:
            for index in reversed(range(len(self.elements) // 2)):
                self._heapify(index)

    def _heapify(self, index: int):
        left = index * 2 + 1
        right = index * 2 + 2
        biggest = index
        if left < len(self.elements):
            try:
                c = comparator_d(self.elements[left], self.elements[biggest])
            except TypeError:
                c = (self.elements[left] > self.elements[index])
            if c:
                biggest = left
        if right < len(self.elements):
            try:
                c = comparator_d(self.elements[right], self.elements[biggest])
            except TypeError:
                c = (self.elements[right] > self.elements[biggest])
            if c:
                biggest = right
        if biggest != index:
            self.elements[index], self.elements[biggest] = \
                self.elements[biggest], self.elements[index]
            self._heapify(biggest)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        extracted = self.elements.pop(0)
        self.build_heap()
        return extracted


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
