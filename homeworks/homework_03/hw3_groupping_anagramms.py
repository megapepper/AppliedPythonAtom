#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    """
    Функция, которая группирует анаграммы.
    Возвращаем массив, где элементом является массив с анаграмами.
    Пример:  '''Аз есмь строка живу я мерой остр
                За семь морей ростка я вижу рост
                Я в мире сирота
                Я в Риме Ариост'''.split()
                ->
                [
                 ['Аз'], ['есмь', 'семь'],
                 ['строка', 'ростка'], ['живу', 'вижу'],
                 ['я', 'я'], ['мерой', 'морей'],
                 ['остр)'], ['За'], ['рост'], ['Я', 'Я'],
                 ['в', 'в'], ['мире'], ['сирота'],
                 ['Риме'], ['Ариост']
                ]
    :param words: list of words (words in str format)
    :return: list of lists of words
    """
    # TODO: реализовать функцию
    groupped_anagrams = []
    for Word in words:
        word = Word.lower()
        letters = set(word)
        for anagrams in groupped_anagrams:
            for anagram in anagrams:
                if (letters == set(anagram.lower())):
                    anagrams.append(Word)
                    Word = None
                break
            if Word is None:
                break
        if Word is not None:
            groupped_anagrams.append([Word])
    return groupped_anagrams
