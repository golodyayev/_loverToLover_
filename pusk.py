from class1 import USER, USERS_DF
from class2 import COUPLE_DF,questions , data,Current_day
import logging
from tockens import tocken_tg as token
from telegram.ext import Updater
from tockens import tocken_vk
from vk_class import server , user_vk, vk_df
from tockens import tocken_vk
import random
import telebot
import time
import library


TYPING_CHOICE1 = 0
TYPING_CHOICE2 = 0
CHOICE1 = 1
CHOICE2 = 1
var1,var2 = 0,1
couple = COUPLE_DF()
USERS_baza = USERS_DF()

vk = server(tocken_vk)

vk_df = vk_df()

bot = telebot.TeleBot(token)
book = library.book

question = questions()
current = Current_day()
data = data()



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token)

from tg_conversation import tg_converastion
from vk_listen import listen
from vk_conversation import vk_con,keyboard_statistic,keyboard_nachat,keyboard_start
from main import sender,keyboard_like,keyboard_statistic,like,markup
print("hoho")


from threading import Thread
from multiprocessing import Process



#vk_con()
#listen()
#tg_converastion(logger,updater,couple, USERS_baza, TYPING_CHOICE1,TYPING_CHOICE2,CHOICE1,CHOICE2,var1,var2)
#sender(data,current,couple,book,bot,vk,keyboard_statistic,keyboard_like,markup,like)



aa = Process(target=vk_con(), args=())

bb = Process(target=listen(), args=())

input2 = [logger,updater,couple, USERS_baza, TYPING_CHOICE1,TYPING_CHOICE2,CHOICE1,CHOICE2,var1,var2]

cc = Process(target=tg_converastion, args=[input2])

input = [data,current,couple,book,bot,vk,keyboard_statistic,keyboard_like,markup,like]
dd = Process(target=sender, args=[input])


aa.start()

bb.start()

cc.start()

dd.start()


aa.join()

bb.join()

cc.join()

dd.join()