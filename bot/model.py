import numpy as np
import gensim
import pymorphy2
from sklearn.neighbors import KNeighborsClassifier
from functools import lru_cache
from gensim.models import KeyedVectors
import pickle
import os
import re


model = KeyedVectors.load('my_model')
morph = pymorphy2.MorphAnalyzer()
clf_file = 'trained_knn.clf'
clf = None


@lru_cache(maxsize=10000)
def get_normal_form(i):
    return morph.normal_forms(i)[0]


def normalize_text(x):
    return ' '.join([get_normal_form(i) for i in re.findall('\w+', x)])


def get_question_vector(question):
    question_vect = np.zeros(300)
    try:
        for word in re.findall('\w+', question):
            question_vect += model.wv.__getitem__(word)
    except KeyError:
        pass
    return question_vect


def train_model():
    quest_dict = dict()
    X = []
    y = []

    block = []
    with open('Otvety.txt') as f:
        for line in f:
            if '---' not in line:
                block.append(line.strip())
            elif len(block) > 1:
                quest_dict[normalize_text(block[0])] = block[1]
                block.clear()
            else:
                block.clear()

    for (key, value) in quest_dict.items():
        answer = value
        question_vect = get_question_vector(key)
        X.append(question_vect)
        y.append(answer)

    clf = KNeighborsClassifier()
    clf.fit(X, y)

    with open(clf_file, 'wb') as f:
        pickle.dump(clf, f)

    return clf


def get_answer(question):
    global clf
    if clf is None:
        if clf_file in os.listdir():
            with open(clf_file, 'rb') as f:
                clf = pickle.load(f)
        else:
            clf = train_model()

    question = normalize_text(question)
    question_vect = get_question_vector(question)
    answer = clf.predict([question_vect])
    return answer[0]


if __name__ == '__main__':
    answer = get_answer('какой-то вопрос')
    print(answer)
