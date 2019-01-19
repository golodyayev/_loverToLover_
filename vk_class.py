import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

import random
from tockens import tocken_vk
import pandas as pd
import numpy as np


def get_random_id():
    return (random.getrandbits(31) * random.choice([-1, 1]))


keyboard_start = VkKeyboard(one_time=True)
keyboard_start.add_button('Join', color=VkKeyboardColor.PRIMARY)
keyboard_start.add_button('Generate', color=VkKeyboardColor.POSITIVE)

keyboard_generate = VkKeyboard(one_time=True)
keyboard_generate.add_button('Прислать код', color=VkKeyboardColor.POSITIVE)

keyboard_nachat = VkKeyboard(one_time=True)
keyboard_nachat.add_button('Начать', color=VkKeyboardColor.POSITIVE)

class user_vk:
    def __init__(self, id):
        self.df = pd.DataFrame(columns=["num", "msg", "date", "stat"])
        self.name = "usr_" + str(id)
        self.id = id
    def apend(self, msg, date):

        try:
            self.df.loc[len(self.df)] = [len(self.df), msg, date, 0]
        except:
            pass

    def prin(self):
        print(self.df.head())

    def write(self):
        self.df.to_csv("vk_data/" + self.name + ".csv")

    def read(self):
        try:
            self.df = pd.read_csv("vk_data/" + self.name + ".csv")[["num", "msg", "date", "stat"]]
        except:
            self.df.to_csv("vk_data/" + self.name + ".csv")
            self.read()


class vk_df:

    def __init__(self):
        self.df = pd.DataFrame(columns=["vk_id", "plus", "active"])
        self.s4et4ik = len(self.df)

    def us_append_unread(self, id):

        dict = [id, 0, 0]
        if len(self.df.loc[self.df.vk_id == id]) == 0:
            try:
                self.df.loc[len(self.df)] = dict
            except IOError:
                return ""
        else:
            self.df.loc[self.df.vk_id == id, "plus"] = 0

    def print(self):
        print(self.df.head())


    def usr_read(self, id):
        self.df.loc[self.df.vk_id == id, "plus"] = 1


    def usr_active(self, id):
        self.df.loc[self.df.vk_id == id, "active"] = 1

    def get_user(self):
        num = self.df.loc[self.df.active == 0]
        return (num.loc[self.df.plus == 0])



    def get_user_1(self):
        try:
            num = self.df.loc[self.df.active == 1]
            return (num.loc[self.df.plus == 0])
        except:
            return(pd.DataFrame(columns=["vk_id", "plus", "active"]))

    def read(self):
        try:
            self.df = pd.read_csv("VK_check.csv")[["vk_id", "plus", "active"]]
        except:
            self.df.to_csv("VK_check.csv")
            self.read()

    def write(self):
        self.df.to_csv("VK_check.csv")


class server:

    def __init__(self, tocken ):

        self._tocken = tocken
        self.vk_session = vk_api.VkApi(token=self._tocken)
        self.vk = self.vk_session.get_api()
        self._upload = VkUpload(self.vk_session)
        self.longpoll = VkLongPoll(self.vk_session)
        self.df = pd.DataFrame()
    def test(self):

        self.vk.messages.send(
                    user_id=154502531,
                    random_id=get_random_id(),

                    message='Это тест отправки, юху'
                )
    def test2(self):

        self.vk.messages.send(
                    user_id=154502531,
                    random_id=get_random_id(),
                    keyboard = keyboard_start.get_keyboard(),
                    message='конверсайшн'
                )


    def send_message(self,user_id,msg,key = None):

        self.vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard = key.get_keyboard(),
            message=msg
                )
    def send_message2(self,user_id,msg):

        self.vk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=msg
                )
    def listen(self,user_vk, vk_df):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                msg = event.text
                usr_id = event.user_id
                time = event.timestamp


                user_vk1 = user_vk(usr_id)
                vk_df1 = vk_df()


                user_vk1.read()
                vk_df1.read()
                user_vk1.apend(msg,time)
                vk_df1.us_append_unread(usr_id)
                vk_df1.print()



                vk_df1.write()
                user_vk1.write()




