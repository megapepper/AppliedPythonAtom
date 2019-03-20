#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self._key = key
            self._value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self._key

        def get_value(self):
            # TODO возвращаем значение
            return self._value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            if self._key == other:
                return True
            return False

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self._buckets_len = bucket_num
        self._buckets = [None] * bucket_num
        self._num_filled_buckets = 0
        self._num_filled_entries = 0

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        index = self._get_index(self._get_hash(key))
        if self._buckets[index] is not None:
            for entry in self._buckets[index]:
                if entry.get_key() == key:
                    return entry.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        try:
            entry = self.Entry(key, value)
            index = self._get_index(self._get_hash(key))
            if self._buckets[index] is None:
                self._buckets[index] = list()
                self._buckets[index].append(entry)
                self._num_filled_buckets += 1
                self._num_filled_entries += 1
            elif self._buckets[index] is not None:
                for iter_entry in self._buckets[index]:
                    if key == iter_entry.get_key():
                        iter_entry._value = value
                        return
                self._buckets[index].append(entry)
                self._num_filled_entries += 1
            if ((self._num_filled_buckets / self._buckets_len) > (2 / 3)):
                self._resize()
        except TypeError as err:
            print(err.__doc__)
            return
        return

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self._num_filled_entries

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        try:
            return hash(key)
        except TypeError:
            raise TypeError

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self._buckets_len

    def values(self):
        # TODO Должен возвращать итератор значений
        return (entry.get_value()
                for bucket in self._buckets if bucket is not None for entry in bucket)

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return (entry.get_key()
                for bucket in self._buckets if bucket is not None for entry in bucket)

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return ((entry.get_key(), entry.get_value())
                for bucket in self._buckets if bucket is not None for entry in bucket)

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        self._buckets_len *= 2
        self._num_filled_buckets = 0
        self._num_filled_entries = 0
        buckets = self.items()
        self._buckets = [None] * self._buckets_len
        for bucket in buckets:
            self.put(bucket[0], bucket[1])

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        res = ''
        for i in range(self._buckets_len):
            res += '[{}]-->['.format(i)
            if self._buckets[i] is None:
                pass
            else:
                for entry in self._buckets[i]:
                    res += '({},{})'.format(entry.get_key(), entry.get_value())
            res += ']\n'
        return res

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        index = self._get_index(self._get_hash(item))
        if self._buckets[index] is not None:
            for entry in self._buckets[index]:
                if entry.get_key() == item:
                    return True
        return False
