from tockens import tocken_tg as token
import uuid

from ppz import MessageHandler2
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler, \
    RegexHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import pandas as pd
def key_gen():
    key = ("key_" + str(uuid.uuid1())[:12])
    return(key)

class Current_day:

    def __init__(self):
        self.df = pd.DataFrame(columns=["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"])
        self.s4et4ik = len(self.df)
    def clear(self):
        self.df = pd.DataFrame(columns=["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"])
    def us_append_couples(self, COUPLE):

        self.df[["couple_id", "user_id1", "user_id2", "key"]] = COUPLE
        # return (self)

    def us_append_question(self, couple_id, key, array):
        self.df.loc[self.df.key == key, "QUESTIONS"] = str(array)


    def us_append_feedback(self, user_id, question, mark):
        print (len(self.df.loc[self.df.user_id1 == user_id]))
        if len(self.df.loc[self.df.user_id1 == user_id]) > 0:
            stolb = str(question+"_1")
            print(stolb)
            self.df.loc[self.df.user_id1 == user_id, "1_1"] = mark

        if len(self.df.loc[self.df.user_id2 == user_id]) > 0:
            stolb = str(question+"_2")
            print(stolb)

            self.df.loc[self.df.user_id2 == user_id, "1_2"] = mark

    def print(self):
        print(self.df.head())

    def read(self):
        try:
            self.df = pd.read_csv("CURRENT_DAY.csv")[
                ["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"]]
        except:
            return ("")

    def write(self):
        self.df.to_csv("CURRENT_DAY.csv")





from class1 import USER, USERS_DF
from class2 import COUPLE_DF,questions , data,Current_day


couple = COUPLE_DF()
USERS_baza = USERS_DF()


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text("Hello chose option",
                              reply_markup=main_menu_keyboard())

def main_menu_keyboard():
    reply_keyboard = [['Join', 'Generate']]
    return  ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def wait_menu_keydoard():
    reply_keyboard = [['Начать', 'Выйти']]
    return  ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def generate_keybord():
    reply_keyboard = [['Прислать код']]
    return  ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def like_keyboard():
    reply_keyboard = [['Like',"Dislike"]]
    return  ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def chosen_keyboard():
    reply_keyboard = [['1',"2"],['3',"4","5"]]
    return  ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)



def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def join(bot, update):
    text = "Вы решили присоедениться к паре \n Вам нужно ввести код полученный от своего друга в формате :key_xxx:"
    update.message.reply_text(text)
    return TYPING_CHOICE1

def find_key(bot, update):
    couple.read()
    t = update.message.text
    k = couple.cheker(t)

    if k == 1:
        USERS_baza.read()

        user_id = "tg_" + str(update.message.chat_id)
        name = update.message.from_user.first_name
        user = USER(name, user_id, key = t)

        USERS_baza.us_append(user)
        couple.us_append2(user)
        update.message.reply_text("Ваш ключ подходит к USER###",reply_markup= wait_menu_keydoard())
        USERS_baza.write()
        couple.write()

        return CHOICE1
    else:
        update.message.reply_text("Ваш ключ не подходит, попробуем еще раз:")

        return TYPING_CHOICE1


def generate(bot, update):
    text = "Вы решили создать пару \n Вам нужно отправить этот код своему визави"
    update.message.reply_text(text, reply_markup= generate_keybord() )
    return TYPING_CHOICE2


def generate_key(bot, update):
    USERS_baza.read()
    couple.read()
    user_id = "tg_"+str(update.message.chat_id)
    key = key_gen()
    name = update.message.from_user.first_name
    user = USER(name, user_id, key=key)
    USERS_baza.us_append(user)
    couple.us_append1(user)
    update.message.reply_text(key, reply_markup= wait_menu_keydoard())
    USERS_baza.write()
    couple.write()
    return CHOICE2




def messg_join(bot, update):
    update.message.reply_text("Вы присоеденились к квесту, ждите навых испытаний",reply_markup= ReplyKeyboardRemove())
    return ConversationHandler.END

def messg_gen(bot, update):
    update.message.reply_text("Вы создали квест, мы ждем второго игрока, а вы ждите навых испытаний",reply_markup= ReplyKeyboardRemove())
    return ConversationHandler.END

def messg_from_main(bot, update):
    update.message.reply_text("Мы пришли сюда по запросу из мэин: какая тема еще интересна: ",reply_markup= chosen_keyboard())

updater = Updater(token)

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_error_handler(error)

TYPING_CHOICE1 = 0
TYPING_CHOICE2 = 0
CHOICE1 = 1
CHOICE2 = 1

conv_handler = ConversationHandler(
    entry_points= [RegexHandler('^(Join)$', join)],
    states = {
        TYPING_CHOICE1: [MessageHandler(Filters.text,
                                       find_key)],
        CHOICE1: [RegexHandler('^Начать$', messg_join)]
    },

    fallbacks = [CommandHandler('cancel', cancel)]
)

conv_handler2 = ConversationHandler(
    entry_points= [RegexHandler('^(Generate)$', generate)],
    states = {
        TYPING_CHOICE2: [RegexHandler('^(Прислать код)$',
                                       generate_key)],
        CHOICE2 :        [RegexHandler('^Начать$', messg_gen)]

    },

    fallbacks = [CommandHandler('cancel', cancel)]
)

def doit(bot, update):
    text = "вот ту короче пока алгоритм закончился но мы тебя записали!!"
    update.message.reply_text(text, reply_markup= ReplyKeyboardRemove() )


dp.add_handler(RegexHandler('^(Done!|Не сделал)$', doit))


def after_choise1_(bot, update):
    print("ghghfh")
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"1",5)
    current.write()

    return var1
def after_choise2_(bot, update):
    print("ghghfh")
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    print(user_id)
    current.us_append_feedback(int(user_id),"2",5)
    current.write()
    current.print()
    return var1
def after_choise3_(bot, update):
    print("ghghfh")
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"3",5)
    current.write()

    return var1
def after_choise4_(bot, update):
    print("ghghfh")
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"4",5)
    current.write()
    return var1
def after_choise5_(bot, update):
    print("ghghfh")
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"5",5)
    current.write()
    return var1








def after_choise_2(bot, update):
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"2",3)
    current.write()
    return var2
def after_choise_1(bot, update):
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"1",3)
    current.write()
    return var2
def after_choise_3(bot, update):
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"3",3)
    current.write()
    return var2
def after_choise_4(bot, update):
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"4",3)
    current.write()
    return var2
def after_choise_5(bot, update):
    text = "Спасибо за выбор, выберите что нить еще прикольное"
    update.message.reply_text(text, reply_markup= chosen_keyboard() )
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"5",3)
    current.write()
    return var2




def after_choise__2(bot, update):
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"2",1)
    current.write()
    update.message.reply_text("ждите короче)_Это конец",reply_markup= ReplyKeyboardRemove())
def after_choise__1(bot, update):
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"1",1)
    current.write()
    update.message.reply_text("ждите короче)_Это конец",reply_markup= ReplyKeyboardRemove())
    return ConversationHandler.END
def after_choise__3(bot, update):
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"3",1)
    current.write()
    update.message.reply_text("ждите короче)_Это конец",reply_markup= ReplyKeyboardRemove())
    return ConversationHandler.END
def after_choise__4(bot, update):
    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"4",1)
    current.write()
    update.message.reply_text("ждите короче)_Это конец",reply_markup= ReplyKeyboardRemove())
    return ConversationHandler.END
def after_choise__5(bot, update):

    current = Current_day()
    current.read()
    user_id = update.message.chat_id
    current.us_append_feedback(user_id,"5",1)
    current.write()
    update.message.reply_text("ждите короче)_Это конец",reply_markup= ReplyKeyboardRemove())
    return ConversationHandler.END

var1,var2 = 0,1





conv_handler3 = ConversationHandler(
    entry_points= [RegexHandler('^(1)$', after_choise1_),
                   RegexHandler('^(2)$', after_choise2_),
                   RegexHandler('^(3)$', after_choise3_),
                   RegexHandler('^(4)$', after_choise4_),
                   RegexHandler('^(5)$', after_choise5_)],
    states = {
        var1: [RegexHandler('^(2)$', after_choise_2),
               RegexHandler('^(1)$', after_choise_1),
               RegexHandler('^(3)$', after_choise_3),
               RegexHandler('^(4)$', after_choise_4),
               RegexHandler('^(5)$', after_choise_5)],

        var2: [RegexHandler('^(2)$', after_choise__2),
               RegexHandler('^(1)$', after_choise__1),
               RegexHandler('^(3)$', after_choise__3),
               RegexHandler('^(4)$', after_choise__4),
               RegexHandler('^(5)$', after_choise__5)]

    },

    fallbacks = [CommandHandler('cancel', cancel)]
)




dp.add_handler(conv_handler)
dp.add_handler(conv_handler2)
dp.add_handler(conv_handler3)

updater.start_polling()

updater.idle()
