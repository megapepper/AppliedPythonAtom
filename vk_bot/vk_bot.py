import bs4 as bs4
import requests


class VkBot:

    def __init__(self, user_id):
        print("Создан объект бота!")

        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ПОГОДА", "ВРЕМЯ", "ПОКА", "ГДЕ"]
        self.autorization_key = "авторизуй"
        self.autorization_users = []

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):
        mes = message
        if mes == self.autorization_key:
            print("{}".format(mes))

            with open("file_users_id.txt", 'a') as f:
                f.write(str(self._USER_ID) + "\n")

            return "Привет, {}!".format(self._USERNAME)
        else:
            user_id = list()
            user_id_int = list()
            with open(
                    "file_users_id.txt", 'r') as f:
                user_id = f.readlines()

            for i in user_id:
                self.autorization_users.append(int(i))
                user_id_int.append(int(i))
                print("".format(user_id_int))

            if self._USER_ID in self.autorization_users:
                # Привет
                if message.upper() == self._COMMANDS[0]:
                    return "Привет-привет, {}!".format(self._USERNAME)

                    # Пока
                elif message.upper() == self._COMMANDS[3]:
                    return "Пока, {}!".format(self._USERNAME)

                    # Пока
                elif message.upper() == self._COMMANDS[4]:
                    return "не знаю, {}!".format(self._USERNAME)
                else:
                    return "Не понимаю о чем ты, но ты классный..."
            else:
                return "Не понимаю о чем вы... напишите {}".format(
                    self.autorization_key)

    @staticmethod
    def _clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
