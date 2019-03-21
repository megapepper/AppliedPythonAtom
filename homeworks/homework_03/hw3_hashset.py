#!/usr/bin/env python
# coding: utf-8
from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self, b=64):
        # TODO Сделать правильно =)
        super().__init__(b)

    def get(self, key):
        # TODO достаточно переопределить данный метод
        return True if key in self else None

    def put(self, key):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, key)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        new_hash_set = HashSet()
        for bucket in another_hashset.values():
            if bucket in self:
                new_hash_set.put(bucket)
        return new_hash_set
