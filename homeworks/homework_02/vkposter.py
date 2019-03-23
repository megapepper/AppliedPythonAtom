#!/usr/bin/env python
# coding: utf-8


class VKPoster:
    """Обработка постов из вк"""

    def __init__(self):
        raise NotImplementedError
        self.subscr = {}  # словарь для подписок   (ключ - user_id)
        self.post = {}  # словарь для публикаций (ключ - post_id) ( массив людей, которые прочитали)
        self.autor = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if post_id not in self.post.keys():
            self.post[post_id] = []
            if user_id not in self.autor.keys():
                self.autor[user_id] = [post_id]  # у одног автора может быть несколько постов
            else:
                self.autor[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        if post_id not in self.post.keys():
            self.user_posted_post(-1, post_id)
        if user_id not in self.post.get(post_id):
            self.post.get(post_id).append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id not in self.subscr.keys():
            self.subscr[follower_user_id] = [followee_user_id]
        else:
            if followee_user_id not in self.subscr[follower_user_id]:
                self.subscr[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        BUFFER = []
        if user_id in self.subscr.keys():
            for i in self.subscr[user_id]:
                if i in self.autor.keys():
                    BUFFER += self.autor[i]
        if len(BUFFER) != 0:
            BUFFER = sorted(BUFFER, reverse=True)
        return BUFFER[:-(len(BUFFER) - k)]

    def get_most_popular_posts(self, k: int) -> list:
        BUFFER = []
        BUFFER = sorted(self.post.keys(), key=lambda ForPost:
        (len(self.post.get(ForPost)), ForPost), reverse=True)
        return BUFFER[:-(len(BUFFER) - k)]
