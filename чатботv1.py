import random, vk_api, vk
import requests
import time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from functools import reduce
from private import token
from models import  AllEmoji
vk_session = vk_api.VkApi(token=token)

longpoll = VkBotLongPoll(vk_session, 201678074)



vk = vk_session.get_api()
arrow_right = '&#10145;'
arrow_left = '&#11013;'
arrow_up = '&#11014;'
arrow_down = '&#11015;'
keyboard = VkKeyboard(one_time=True)
keyboard.add_button(arrow_left, color=VkKeyboardColor.NEGATIVE)
keyboard.add_button(arrow_right, color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button(arrow_up, color=VkKeyboardColor.NEGATIVE)
keyboard.add_button(arrow_down, color=VkKeyboardColor.POSITIVE)

#keyboard.add_line()
#keyboard.add_location_button()
#keyboard.add_line()
#keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=201678074")
#'____________________________\n'
#white_square = '&#9643;'
white_square = '▫'
zero_emoji = '0&#8419;'
space = '&#12288;'
square_line = white_square * 9 + '\n'
space_line = space * 28 + '\n'
square_space_line = square_line + space_line
map_matrix = [['0&#8419;'] * 9] * 9
zefirchik = '&#128527;'
current_place = [4,4]


'⬅➡⬆⬇'


#map_matrix[4][4] = zefirchick эта хуйня не работает из-за сылок списка
#map_matrix[4] = map_matrix[4][:4] + [zefirchik] + map_matrix[4][5:]
#print(map_matrix)
map_str = ''
for line in map_matrix:
    map_line = reduce(lambda x, y: x+y, line) + '\n'
    map_line += space_line
    map_str += map_line

def change_symbol(matrix_map, colmn, line, symbol):
    matrix_map[line] = matrix_map[line][:colmn] + [symbol] + matrix_map[line][colmn+1:]
    map_str = ''
    for lst in matrix_map:
        map_line = reduce(lambda x, y: x+y, lst) + '\n'
        map_line += space_line
        map_str += map_line
    return map_str

map_str = change_symbol(map_matrix, 4, 4, zefirchik)

#print(map_str)
#print(len(game_map))
#print(len('___________________________'))
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'карта' in str(event):
            if event.from_chat:
                    rand_id = get_random_id()
                    #emoji_map = map_str
                    #emoji_map = white_square * 9 + '\n' + space * 28 + '\n' + white_square * 9 + '\n' + space * 28 + '\n'
                    vk.messages.send(
                    key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                    server = ('https://lp.vk.com/wh201678074'),
                    ts=('1'),
                    random_id = rand_id,
              	    message = map_str,
            	    chat_id = event.chat_id
                    )
        if 'зефирчик' in str(event):
            if event.from_chat:
                    col = int(event.object['text'][-1])
                    ln =  int(event.object['text'][-3])
                    #print(event.object['text'])
                    rand_id = get_random_id()
                    emoji_map = change_symbol(map_matrix, col-1, ln-1, zefirchik)
                    #emoji_map = white_square * 9 + '\n' + space * 28 + '\n' + white_square * 9 + '\n' + space * 28 + '\n'
                    vk.messages.send(
                    key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                    server = ('https://lp.vk.com/wh201678074'),
                    ts=('1'),
                    random_id = rand_id,
              	    message = emoji_map,
            	    chat_id = event.chat_id
                    )

        if 'клава' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard = keyboard.get_keyboard(),
                    key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                    server = ('https://lp.vk.com/wh201678074'),
                    ts=('1'),
                    random_id = get_random_id(),
              	    message='вот кнопки',
             	    chat_id = event.chat_id
            	    )
        if '➡' == event.object['text'][-1]:
            if event.from_chat:
                    if current_place[0] +1 > 8:
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = 'Ты дошёл до края карты!\n' + map_str,
                        chat_id = event.chat_id
                        )
                       
                    else:    
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        current_place[0] +=1
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = map_str,
                        chat_id = event.chat_id
                        )
        if '⬆' == event.object['text'][-1]:
            if event.from_chat:
                    if current_place[1] -1 < 0:
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = 'Ты дошёл до края карты!\n' + map_str,
                        chat_id = event.chat_id
                        )
                    else:    
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        current_place[1] -=1
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = map_str,
                        chat_id = event.chat_id
                        )
        if '⬇' == event.object['text'][-1]:
            if event.from_chat:
                    if current_place[1] +1 > 8:
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = 'Ты дошёл до края карты!\n' + map_str,
                        chat_id = event.chat_id
                        )
                    else:    
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        current_place[1] +=1
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = map_str,
                        chat_id = event.chat_id
                        )
        if '⬅' == event.object['text'][-1]:
            if event.from_chat:
                    if current_place[0] -1 < 0:
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = 'Ты дошёл до края карты!\n' + map_str,
                        chat_id = event.chat_id
                        )
                    else:    
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], white_square)
                        current_place[0] -=1
                        #emoji_map = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        map_str = change_symbol(map_matrix, current_place[0], current_place[1], zefirchik)
                        rand_id = get_random_id()
                        vk.messages.send(
                        keyboard = keyboard.get_keyboard(),
                        key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                        server = ('https://lp.vk.com/wh201678074'),
                        ts=('1'),
                        random_id = rand_id,
                        message = map_str,
                        chat_id = event.chat_id
                        )
'''
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'карта' in str(event):
            if event.from_chat:
                    #emoji_map = (zero_emoji * 9 + '\n') * 9,
                    emoji_map = zero_emoji * 9 + '\n' + '___________________________\n' + zero_emoji * 9 + '\n' + '___________________________\n',
                    vk.messages.send(
                    key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          
                    server = ('https://lp.vk.com/wh201678074'),
                    ts=('1'),
                    random_id = get_random_id(),
              	    message = emoji_map,
            	    chat_id = event.chat_id
                    )
                    
'''


'''
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = ('https://lp.vk.com/wh201678074'),
                    ts=('1'),
                    random_id = get_random_id(),
              	    message='Привет!',
            	    chat_id = event.chat_id
                    )
        if 'Клавиатура' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard = keyboard.get_keyboard(),
                    key = ('46c814dccc28951c212c1a736c4883e46bbc0423'),          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = ('https://lp.vk.com/wh201678074'),
                    ts=('1'),
                    random_id = get_random_id(),
              	    message='Держи',
             	    chat_id = event.chat_id
            	    )

for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars1 = ['Привет', 'Ку', 'Хай', 'Хеллоу']
        if event.text in vars1:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    message = 'Привет)',
                    random_id = get_random_id()
                    )
        vars2 = ['Клавиатура', 'клавиатура']
        if event.text in vars2:
            if event.from_user:
                Lsvk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),


                    keyboard = keyboard.get_keyboard(),
                    message = 'Держи'
                    )
'''
