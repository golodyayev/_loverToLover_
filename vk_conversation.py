from vk_class import server , user_vk, vk_df
from tockens import tocken_vk
import numpy as np
from time import sleep
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import uuid

from class1 import USER, USERS_DF
from class2 import COUPLE_DF,questions , data,Current_day

def key_gen():

    key = ("key_" + str(uuid.uuid1())[:12])
    return(key)

def find_bool(bl):
    for idx, i in enumerate(bl):
        if i:
            return (idx)

keyboard_statistic = VkKeyboard(one_time=True)
keyboard_statistic.add_button('1', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_button('2', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_button('3', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_line()
keyboard_statistic.add_button('4', color=VkKeyboardColor.POSITIVE)
keyboard_statistic.add_button('5', color=VkKeyboardColor.POSITIVE)


keyboard_start = VkKeyboard(one_time=True)
keyboard_start.add_button('Join', color=VkKeyboardColor.PRIMARY)
keyboard_start.add_button('Generate', color=VkKeyboardColor.POSITIVE)

keyboard_generate = VkKeyboard(one_time=True)
keyboard_generate.add_button('Прислать код', color=VkKeyboardColor.POSITIVE)

keyboard_nachat = VkKeyboard(one_time=True)
keyboard_nachat.add_button('Начать', color=VkKeyboardColor.POSITIVE)



vk = server(tocken_vk)
couple = COUPLE_DF()
USERS_baza = USERS_DF()
vk_df = vk_df()

def massage_handler(user):

    user.read()
    #if True:
    try:
        print("nen")
        first = np.array(user.df.loc[user.df.stat == 0, "msg"])[0]
        bl = (user.df.stat == 0)
        xxx = find_bool(bl)
        if len(first)>0 :
            print (first)
            if first == "/start":
                vk.send_message(user.id, "Hello chose the option", keyboard_start)

            elif first == "Generate":
                vk.send_message(user.id, "Вам нужно прислать код своему визави", keyboard_generate)

            elif first == "Прислать код":
                kod = key_gen()

                USERS_baza.read()
                couple.read()
                user_id = "vk_" + str(user.id)

                name = "from_vk_noname"

                users = USER(name, user_id, key=kod)
                USERS_baza.us_append(users)
                couple.us_append1(users)

                USERS_baza.write()
                couple.write()
                #user_gener
                #couple_gen

                vk.send_message(user.id, kod, keyboard_nachat)
            elif first == "Начать":
                vk_df.usr_active(user.id)
                vk.send_message2(user.id, "вcё сделано, ждите")


            elif first == "Join":
                vk.send_message2(user.id, "введи код полученный от визвави")

            else:
                m1 = user.df.loc[xxx-1 , "msg"]
                m2 = user.df.loc[xxx-2 , "msg"]
                print (m1,m2,"m1m2")
                if m1 == "Join" or m2 == "Join":


                    USERS_baza.read()
                    couple.read()
                    key = first
                    if couple.cheker(key) == 1:
                        user_id = "vk_" + str(user.id)
                        name = "from_vk"
                        users = USER(name, user_id, key=key)
                        USERS_baza.us_append(users)
                        couple.us_append2(users)
                        vk.send_message2(user.id, "вcё сделано, ждите")
                        vk_df.usr_active(user.id)
                        USERS_baza.write()
                        couple.write()
                    else:
                        print("fddd")
                        vk.send_message2(user.id, "код не подошел, попробуй еще")
                        user.df.loc[xxx] = None
                        user.df = user.df.dropna()
                        user.write()
                        USERS_baza.write()
                        couple.write()
                        massage_handler(user)

                    #check key
                    #users to couple
                    #waiting list

                else:

                    vk.send_message2(user.id, "чет не понял, сорян")



            user.df.loc[xxx, "stat"] = 1
            print(user.df)
            user.write()
            massage_handler(user)
        else :

            return()
    #try: print(1)
    except Exception as e:
        print(e)
        return()

def find(a1,a2,a3,a4):
    kol = 0
    for i in [a1,a2,a3,a4]:
        try:
            int(i)
            kol += 1
        except:
            pass
    return(kol)

def piwu_pismo(first, text, x):
    if first == "1":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "1", x)
        current.write()
        vk.send_message(user.id, text, keyboard_statistic)
    elif first == "2":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "2", x)
        current.write()
        vk.send_message(user.id, text, keyboard_statistic)
    elif first == "3":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "3", x)
        current.write()
        vk.send_message(user.id, text, keyboard_statistic)
    elif first == "4":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "4", x)
        current.write()
        vk.send_message(user.id, text, keyboard_statistic)
    elif first == "5":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "5", x)
        current.write()
        vk.send_message(user.id, text, keyboard_statistic)
    else:
        vk.send_message2(user.id, "чет не понял, сорян")



def piwu_pismo2(first,text, x):
    if first == "1":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "1", x)
        current.write()
        vk.send_message2(user.id, text)
    elif first == "2":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "2", x)
        current.write()
        vk.send_message2(user.id, text)
    elif first == "3":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "3", x)
        current.write()
        vk.send_message2(user.id, text)
    elif first == "4":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "4", x)
        current.write()
        vk.send_message2(user.id, text)
    elif first == "5":
        current = Current_day()
        current.read()
        current.us_append_feedback_vk(user.id, "5", x)
        current.write()
        vk.send_message2(user.id, text)
    else:
        vk.send_message2(user.id, "чет не понял, сорян")

def massage_handler_1(user):
    user.read()
    # if True:
    try:
        print("ятуту")
        first = np.array(user.df.loc[user.df.stat == 0, "msg"])[0]
        bl = (user.df.stat == 0)
        xxx = find_bool(bl)
        if len(first) > 0:
            print(first)
            m1 = user.df.loc[xxx - 1, "msg"]
            m2 = user.df.loc[xxx - 2, "msg"]
            m3 = user.df.loc[xxx - 3, "msg"]
            m4 = user.df.loc[xxx - 4, "msg"]

            kol = find(m1,m2,m3,m4)
            if kol == 0:
                text = "Спасибо за выбор, выберите что нить еще прикольное"
                piwu_pismo(first,text, 5)
            elif kol == 1:
                text = "Спасибо за выбор, выберите что нить еще прикольное"
                piwu_pismo(first,text, 3)

            elif kol == 2:
                text = "ну всё, ждите"
                piwu_pismo2(first,text, 1)
            else:

                vk.send_message2(user.id, "чет не понял, сорян")

            user.df.loc[xxx, "stat"] = 1
            print(user.df)
            user.write()
            massage_handler(user)
        else:

            return ()
    # try: print(1)
    except Exception as e:
        print(e)
        return ()
def main(vk,couple,USERS_baza,vk_df):
    while True:
        if True:
            sleep(1)
            vk_df.read()
            vk_df.print()
            for id in range(len(vk_df.get_user())):
                dd = np.array(vk_df.get_user().loc[id])
                user = user_vk(dd[0])

                massage_handler(user)
                vk_df.usr_read(dd[0])
                del user

            for id in range(len(vk_df.get_user_1())):
                dd = np.array(vk_df.get_user_1().loc[id])
                user = user_vk(dd[0])

                massage_handler_1(user)
                vk_df.usr_read(dd[0])
                del user

            vk_df.write()


#main(vk,couple,USERS_baza,vk_df)


import threading


t1 = threading.Thread(target=main, args=(vk,couple,USERS_baza,vk_df))
t1.start()

t2 = threading.Thread(target=vk.listen, args = (user_vk, vk_df))
t2.start()