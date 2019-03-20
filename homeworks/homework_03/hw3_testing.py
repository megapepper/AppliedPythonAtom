#!/usr/bin/env python
# coding: utf-8
import os
import shutil


class Requester:
    '''
    Какой-то класс, который умеет делать запросы
     к удаленному серверу
    '''

    def get(self, host, port, filename):
        return "Fail"

    def post(self, host, port, filename, data):
        return False


class RemoteFileReader(Requester):
    '''
    Класс для работы с файлами на удаленном сервере
    '''

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def read_file(self, filename):
        return super().get(self._host, self._port, filename)

    def write_file(self, filename, data):
        return super().post(self._host, self._port, filename, data)


class OrdinaryFileWorker(RemoteFileReader):
    '''
    Класс, который работает как с локальными
     так и с удаленными файлами
    '''

    def transfer_to_remote(self, filename):
        with open(filename, "r") as f:
            super().write_file(filename, f.readlines())

    def transfer_to_local(self, filename):
        with open(filename, "w") as f:
            f.write(super().read_file(filename))


class MockOrdinaryFileWorker(OrdinaryFileWorker):
    '''
    Необходимо отнаследовать данный класс так, чтобы
     он вместо запросов на удаленный сервер:
      при transfer_to_remote считывал filename
     из локальной директории ./test_dir и сохранял filename.tmp
     в локальной директории ./tmpf
      при transfer_to_local считывал filename.tmp
     из локальной директории ./test_dir и сохранял в filename
     в локальной директории ./tmpf
      при удалении объекта директория ./tmp должна удаляться
      при создании объекта, директория ./tmp должна создаваться
     если еще не создана
    '''

    def __init__(self):
        '''try:
            os.mkdir('./tmpf')
        except FileExistsError:
            pass'''
        raise NotImplementedError

    def __del__(self):
        try:
            shutil.rmtree('./tmpf')
        except FileNotFoundError:
            pass

    def transfer_to_local(self, filename):
        with open('homeworks/homework_03/test_dir/' + filename + '.tmp', 'r') as f1:
            with open('./tmpf/' + filename, 'w') as f2:
                f2.writelines(f1.read())

    def transfer_to_remote(self, filename):
        with open('homeworks/homework_03/test_dir/' + filename, 'r') as f1:
            with open('./tmpf/' + filename + '.tmp', 'w') as f2:
                f2.writelines(f1.read())


class LLNode:
    def __init__(self, value, next_node):
        """
        Entity (or node) for doubly linked list
        :param value: object
        :param next_node: LLEntity
        """
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "value: {}; next_node: ({})".format(self.value, self.next_node)