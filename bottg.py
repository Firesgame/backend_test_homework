import telebot
from telebot import types
from random import choice, randint
import requests
from translate import Translator

config = '1440643344:AAHZdro5cbSPwyy_Q5Rvs2yhcbnubPFVRxE'

bot = telebot.TeleBot(config)
wishes = ['Если думаешь - не говори', 'Секрет успешного продвижения — это начало', 'Всё будет хорошо',
          'День будет удачным', 'Вас ожидают перемены',
          'Сегодня как раз наступило то завтра, о котором вы беспокоились вчера']


def what_weather(city):
    search = {
        '0': '',
        'T': '',
        'M': '',
    }
    requests_headers = {
        'Accept-Language': 'ru'
    }
    translator = Translator(from_lang="ru", to_lang="en")
    url = ("https://wttr.in/" + translator.translate(city))
    try:
        response = requests.get(url, params=search, headers=requests_headers)
        if response.status_code == 200:
            result = response.text
            print(result)
            return result
        else:
            return "ошибка на сервере"

    except requests.ConnectionError:
        return 'Не робит'


@bot.message_handler(commands=['start'])
def welcome_message(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton('Погода', callback_data='WEATH'),
        types.InlineKeyboardButton('Предсказание', callback_data='FUTURE'),
        types.InlineKeyboardButton('Рандом', callback_data='RANDOM'),
        types.InlineKeyboardButton('Отправить сообщение', callback_data='SEND')
    )
    params = {
        'text': '*Choose button*',
        'reply_markup': keyboard,
        "parse_mode": 'MarkDownV2'
    }

    bot.send_message(**params, chat_id=message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == 'WEATH')
def Pogoda1(call):
    msg = bot.reply_to(call.message, 'Ваш город')
    bot.register_next_step_handler(msg, Pogoda2)


@bot.message_handler(commands=['srazu'])
def Pogoda2(message):
    bot.send_message(message.chat.id, what_weather(message.text))


@bot.callback_query_handler(func=lambda call: call.data == 'FUTURE')
def future(call):
    msg = bot.reply_to(call.message, choice(wishes))


@bot.callback_query_handler(func=lambda call: call.data == 'RANDOM')
def random(call):
    msg = bot.reply_to(call.message, randint(0, 6))


@bot.callback_query_handler(func=lambda call: call.data == 'SEND')
def id(call):
    msg = bot.reply_to(call.message, 'Введите id адресата, текст сообщения')
    bot.register_next_step_handler(msg, id2)


@bot.message_handler(commands=['check'])
def id2(message):
    message = message.text.split(', ', maxsplit=1)
    id = message[0]
    message = message[1]
    bot.send_message(int(id), message)


bot.polling(none_stop=True)
