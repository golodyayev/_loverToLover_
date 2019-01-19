import requests
from tockens import tocken_vk
import random
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

def get_random_id():
    return (random.getrandbits(31) * random.choice([-1, 1]))


keyboard_main = VkKeyboard(one_time=True)

keyboard_main.add_button('Join', color=VkKeyboardColor.PRIMARY)
keyboard_main.add_button('Generate', color=VkKeyboardColor.POSITIVE)



keyboard_join = VkKeyboard(one_time=True)

keyboard_join.add_button('Join', color=VkKeyboardColor.PRIMARY)
keyboard_join.add_button('Generate', color=VkKeyboardColor.POSITIVE)



def main():
    vk_session = vk_api.VkApi(token=tocken_vk)
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
            if event.text == "/start":
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Это супер пупер бот и вы станите счастливы'
                )
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard_main.get_keyboard(),
                    message='Hello chose option'
                )

                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
                        print ("тут")
                        if event.text == "Join":
                            vk.messages.send(
                            user_id=event.user_id,
                         random_id=get_random_id(),
                        message='Введите ключ '
                 )




if __name__ == '__main__':
    main()