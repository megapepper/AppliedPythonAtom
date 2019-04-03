import sys
import requests
import csv
from bs4 import BeautifulSoup
from collections import Counter
import asyncio


@asyncio.coroutine
def parse(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    user_list_ = soup.findAll("span", attrs={
        "class": "user-info__nickname user-info__nickname_small user-info__" +
                 "nickname_comment"})
    user_list = [x.contents[0] for x in user_list_]
    if len(user_list) < 100:
        return 0
    else:
        user_count_dict = Counter(user_list).most_common()
        user_count_dict.sort(key=lambda x: (-x[1], x[0]))
        temp = []
        output = []
        for i in range(len(user_count_dict)):
            temp.append(link)
            temp.append(user_count_dict[i][0])
            temp.append(user_count_dict[i][1])
            output.append(temp)
            temp = []
        with open('top_user_comments.csv', 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(output)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    # Ваш код
    lop = asyncio.get_event_loop()
    task = [asyncio.ensure_future(parse(i)) for i in links]
    wait = asyncio.wait(task)
    lop.run_until_complete(wait)
    lop.close()
