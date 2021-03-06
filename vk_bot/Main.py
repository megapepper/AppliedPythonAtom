import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# --
from commander.commander import Commander
from vk_bot import VkBot
# --
import random


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,
                                "random_id": random.randint(0, 1000)})


# API-ключ созданный ранее
token = "5d1d08c4b4b739b6718b5a9a09aa71332ba4f687aa58321344f706b4351c2a470d3a9011ad64e312dad30"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

commander = Commander()
print("Server started")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)

            if event.text[0] == "/":
                write_msg(event.user_id, commander.do(event.text[1::]))
            else:
                write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
