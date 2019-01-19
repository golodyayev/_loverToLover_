
token='736540653:AAH8hiaDsplxZHm92muhs3lI0MWkhIbDVbs'
from ppz import MessageHandler2
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler, \
    RegexHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging


from class1 import USER, USERS_DF
from class2 import COUPLE_DF




couple = COUPLE_DF()
USERS_baza = USERS_DF()


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token)


updater2 = Updater(token)
############################### Bot ############################################
def main(updater):
    USERS_baza.read()
    couple.read()
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='new'))
    updater.dispatcher.add_handler(CallbackQueryHandler(info, pattern='info'))
    updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='join'))
    updater.dispatcher.add_handler(MessageHandler2(Filters.text, echo, pattern='join'))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()



def wait(key):
    USERS_baza.write()
    couple.write()
    print("wait")
    print("dsfdsfs")

    updater.dispatcher.add_handler(CallbackQueryHandler(wait_menu))

    print("2")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start(bot, update):
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())


def main_menu(bot, update):
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                     message_id=query.message.message_id,
                     text=main_menu_message(),
                     reply_markup=main_menu_keyboard())

def wait_menu(bot, update):
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                     message_id=query.message.message_id,
                     text=main_menu_message(),
                     reply_markup=wait_menu_key())
def wait_menu_key():
    keyboard = [[InlineKeyboardButton('Info', callback_data='info')],
                [InlineKeyboardButton('YOU_shoudle', callback_data='sheudle')]]

    return ReplyKeyboardMarkup(keyboard)

def main_menu_message():
    return 'Choose the option to continue: \n' \
           'либо создай ключ для входа либо войди с чужого'


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Generate', callback_data='new')],
                [InlineKeyboardButton('Join', callback_data='join')]]
    return InlineKeyboardMarkup(keyboard)


def first_menu(bot, update):
    query = update.callback_query

    print(query.message.chat_id)
    print("user generate new nonactive couple")
    user_id = query.message.chat_id
    key = "key_"+ str(query.message.chat_id)
    name = "none"
    user = USER(name, user_id, key=key)
    USERS_baza.us_append(user)
    couple.us_append1(user)


    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text="Вы решили создать новую пару, пришлите этот код своей половинке")

    bot.send_message(chat_id=query.message.chat_id,
                     message_id=query.message.message_id,
                     text= key, callback_data = "wait"
                     )
    wait(1)

def info_keyboard():
    keyboard = [[InlineKeyboardButton('Узнать че вообще тут твориться', callback_data='info')]]
    return InlineKeyboardMarkup(keyboard)


def info(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text="это нужно для товалрвырапвыароиыварьиывьаиывавыьаиывб ваш код все тот же{}".format(
                              query.message.chat_id),
                          reply_markup=info_keyboard())

def echo2(bot, update):
    t = update.message.text
    print("echo2222")
    update.message.reply_text("послали сообщение в вэйте{}".format(t))


def echo(bot, update):
    print("echo")
    t = update.message.text
    print(t[:4])
    if t[:4] == "key_":
        update.message.reply_text("connect with you pair:")
        user_id = update.message.chat_id
        key = t
        name = "none"
        user = USER(name, user_id, key=key)
        USERS_baza.us_append(user)
        couple.us_append2(user)


        wait(1)


def second_menu(bot, update):
    query = update.callback_query

    print(query.message.chat_id)
    print("user try to join couple")

    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text="Вы решили присоедениться к пару пару, введите код полученный от неё:")

def shutdown():
    updater.stop()
    updater.is_idle = False

main(updater)