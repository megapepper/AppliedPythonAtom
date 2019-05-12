import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import model
from bs4 import BeautifulSoup
import requests

COMMANDS = ["ПРИВЕТ", "ПОКА"]
autorization_key = "АВТОРИЗУЙ"
autorization_users = []
token = "5d1d08c4b4b739b6718b5a9a09aa71332ba4f687aa58321344f706b4351c2a470d3a9011ad64e312dad30"


def login_vk(token=None, login=None, password=None):
    if token:
        vk_session = vk_api.VkApi(token=token)
    elif login and password:
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)

    return vk_session


def get_user_name(user_id):
    request = requests.get("https://vk.com/id" + str(user_id))
    bs = BeautifulSoup(request.text, "html.parser")

    result = ""
    not_skip = True
    for i in list(bs.findAll("title")[0]):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True

    return result.split()[0]


vk_session = login_vk(token=token)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            message = "Здравствуй, {}!".format(get_user_name(event.user_id))
            if event.text.upper() == autorization_key:
                print("{}".format(event.text.upper()))

                with open("file_users_id.txt", 'a') as f:
                    f.write(str(event.user_id) + "\n")
                vk.messages.send(user_id=event.user_id,
                                 message=message,
                                 random_id=random.randint(0, 1000))
            else:
                user_id1 = list()
                user_id_int = list()
                with open("file_users_id.txt", 'r') as f:
                    user_id1 = f.readlines()

                for i in user_id1:
                    autorization_users.append(int(i))
                    user_id_int.append(int(i))
                    print("".format(user_id_int))

                if event.user_id in autorization_users:

                    if event.text.upper() == COMMANDS[0]:
                        vk.messages.send(user_id=event.user_id,
                                         message=message,
                                         random_id=random.randint(0, 1000))
                    elif event.text.upper() == COMMANDS[1]:
                        message = "Пока, {}!".format(
                            get_user_name(event.user_id))
                        vk.messages.send(user_id=event.user_id,
                                         message=message,
                                         random_id=random.randint(0, 1000))
                    else:
                        vk.messages.send(user_id=event.user_id,
                                         message=model.get_answer(event.text),
                                         random_id=random.randint(0, 1000))
                else:
                    message1 = "Не понимаю о чем вы... напишите {}".format(
                        autorization_key)
                    vk.messages.send(user_id=event.user_id,
                                     message=message1,
                                     random_id=random.randint(0, 1000))
