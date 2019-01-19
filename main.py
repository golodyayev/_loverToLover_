import random
import telebot
import time
import library
import datetime
from  time import sleep
from tockens import tocken_tg as token
from vk_class import server , user_vk, vk_df
from tockens import tocken_vk
import numpy as np
from time import sleep
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


vk = server(tocken_vk)
bot = telebot.TeleBot(token)
book = library.book
import pandas as pd



keyboard_statistic = VkKeyboard(one_time=True)
keyboard_statistic.add_button('1', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_button('2', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_button('3', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_line()
keyboard_statistic.add_button('4', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_button('5', color=VkKeyboardColor.POSITIVE)

keyboard_like = VkKeyboard(one_time=True)
keyboard_like.add_button('Done!', color=VkKeyboardColor.POSITIVE)
keyboard_like.add_button('Не сделал', color=VkKeyboardColor.NEGATIVE)

from telebot import types
markup = types.ReplyKeyboardMarkup()
markup.row('1', '2')
markup.row('3', '4', '5')

like = types.ReplyKeyboardMarkup()
like.row('Done!','Не сделал')

print (random.randint(0,len(book)))

from class2 import COUPLE_DF,questions , data,Current_day

couple = COUPLE_DF()
question = questions()
current = Current_day()
data = data()

while True:
    print (int(datetime.datetime.now().strftime('%M')))
    t = 1.5
    if t>1:


        couple.read()
        current.read()
        current.clear()
        couples = couple.get_couple()
        current.us_append_couples(couple.get_couple()[["couple_id", "user_id1", "user_id2", "key"]])
        current.write()
        print(datetime.datetime.now())

        for i in range(len(couples)):
            #change id identify from vk/tg
            user1 = str(couples.iloc[i][2])
            user2 = str(couples.iloc[i][1])
            print (user1,user2)
            co_id = str(couples.iloc[i][0])
            co_key = str(couples.iloc[i][3])

            num1 = random.randint(0,len(book)-1)
            num2 = random.randint(0,len(book)-1)
            num3 = random.randint(0,len(book)-1)
            num4 = random.randint(0,len(book)-1)
            num5 = random.randint(0,len(book)-1)


            current.us_append_question(str(co_id),str(co_key), str([num1,num2,num3,num4,num5]))

            print("ff")
            task = '\n – '.join([book[num1],book[num2],book[num3],book[num4],book[num5]])
            send = "Ваше задание на сегодня: \n – {}".format(task)

            if user1[:2] == "tg":
                bot.send_message(user1[3:], text=send)
            else:
                vk.send_message2(user1[3:],send)

            if user2[:2] == "tg":
                bot.send_message(user2[3:], text=send)
            else:
                vk.send_message2(user2[3:],send)


            send2 = "выберите задание которое вы бы хотели выболнить больше всего"
            if user1[:2] == "tg":
                bot.send_message(user1[3:], text=send2, reply_markup=markup)
            else:
                vk.send_message(user1[3:],send2,keyboard_statistic)

            if user2[:2] == "tg":
                bot.send_message(user2[3:], text=send2, reply_markup=markup)
            else:
                vk.send_message(user2[3:], send2, keyboard_statistic)


            print("Send task #XXXXXX to {} ".format(couples.iloc[i][0]))
            current.write()


        sleep(120)

        if t>1:



            couple.read()
            current.read()
            couples = couple.get_couple()

            extract = current.extract()
            data.read()
            data.uppend(current.df)
            data.write()

            for i in range(len(couples)):
                user1 = str(couples.iloc[i][2])
                user2 = str(couples.iloc[i][1])
                number = int(extract.loc[i]["number"])
                print("send final task")
                task = book[number]
                send = "Сегодня вы с вашей парой выполните следующую фигню: \n – {}".format(task)
                if user1[:2] == "tg":
                    bot.send_message(user1[3:], text=send, reply_markup=like)
                else:
                    vk.send_message(user1[3:], send, keyboard_statistic)

                if user2[:2] == "tg":
                    bot.send_message(user2[3:], text=send, reply_markup=like)
                else:
                    vk.send_message(user2[3:], send, keyboard_statistic)





                print("Send finaltask yooohooo #XXXXXX to {} ".format(couples.iloc[i][0]))
                current.write()


        sleep(120)
