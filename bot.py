# -*- coding: utf-8 -*-

import os
import telebot
from telebot import types
from flask import Flask, request
import config
import match
import requests
import json 
import datetime

bot = telebot.TeleBot(config.token)
server = Flask(__name__)
TOKEN = config.token

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_menu.row('Расписание группы')
markup_menu.row('Изменение расписания')
markup_menu.row('Собственное расписание')
markup_menu.row('Информация о вузе')

markup_schedule = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_schedule.row('Сегодня', 'Завтра')
markup_schedule.row('Понедельник', 'Вторник', 'Среда')
markup_schedule.row('Четверг', 'Пятница', 'Суббота')
markup_schedule.row('Назад')

markup_info = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_info.row('Основные сайты')
markup_info.row('Группы Вконтакте')
markup_info.row('Информация о корпусах')
markup_info.row('Назад')

markup_corps = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_corps.row('Корпус А', 'Корпус Б', 'Корпус В', 'Корпус Г')
markup_corps.row('Корпус Д','Корпус Е','Корпус И','Корпус К',)
markup_corps.row('Назад')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, введите группу (Пример КТбо2-3)")
    handle_group(message)

@bot.message_handler(content_types=['text'])
def handle_group(message):
   if message.text:
      bot.send_message(message.chat.id, message.text, reply_markup=markup_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
   if message.text == "1":
      bot.send_message(message.chat.id, "Ну и нахуя", reply_markup=markup_menu)
   elif message.text == "Расписание группы":
      bot.send_message(message.chat.id, "Выберите день", reply_markup=markup_schedule)
   elif message.text == "Информация о вузе":
      bot.send_message(message.chat.id, "Какая информация вам инетересна?", reply_markup=markup_info)
   elif message.text == "Информация о корпусах":
      bot.send_message(message.chat.id, "Выберете корпус", reply_markup=markup_corps)
   elif message.text == "Сегодня":
      day = get_day_of_week(True)
      text = get_schedule(day)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Завтра":
      day = get_day_of_week(False)
      text = get_schedule(day)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Понедельник":
      text = get_schedule('Пнд')
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Вторник":
      text = get_schedule('Втр')
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule) 
   elif message.text == "Среда":
      text = get_schedule('Срд')
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Четверг":
      text = get_schedule('Чтв')
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Пятница":
      text = get_schedule('Птн')
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Суббота":
      text = get_schedule('Сбт')
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Основные сайты":
      text = '\u25b6\ufe0f [<Личный кабинет студента>](<https://sfedu.ru/www/stat_pages22.show?p=STD/lks/D>)\n\u25b6\ufe0f [<LMS>](<https://lms.sfedu.ru>)\n\u25b6\ufe0f [<БРС>](<https://grade.sfedu.ru/>)\n\u25b6\ufe0f [<Сайт ИКТИБа>](<http://ictis.sfedu.ru/>)\n\u25b6\ufe0f [<Проектный офис ИКТИБ>](<https://proictis.sfedu.ru/>)'
      bot.send_message(message.chat.id, text, parse_mode='MarkdownV2', reply_markup=markup_info)
   elif message.text == "Группы Вконтакте":
      text = '\u27a1\ufe0f [<Физическая культура в ИТА ЮФУ>](<https://vk.com/club101308251>)\n\u27a1\ufe0f [<Подслушано в ЮФУ>](<https://vk.com/overhearsfedu>)\n\u27a1\ufe0f [<ИКТИБ ЮФУ>](<https://vk.com/ictis_sfedu>)\n\u27a1\ufe0f [<Студенческий клуб ИТА ЮФУ (г. Таганрог)>](<https://vk.com/studclub_tgn>)\n\u27a1\ufe0f [<Студенческий киберспортивный клуб ЮФУ>](<https://vk.com/esports_sfedu>)\n\u27a1\ufe0f [<Культура здоровья в ИТА ЮФУ>](<https://vk.com/club150688847>)\n\u27a1\ufe0f [<ПервокурсникиУ>](<https://vk.com/1kurs_ita_2019>)\n\u27a1\ufe0f [<Технологии + Проекты + Инновации → ИКТИБ>](<https://vk.com/proictis>)\n\u27a1\ufe0f [<Волонтерский центр ИКТИБ ЮФУ>](<https://vk.com/ictis_vol>)'
      bot.send_message(message.chat.id, text, parse_mode='MarkdownV2', reply_markup=markup_info)
   elif message.text == "Корпус А":
      text = "Таганрог, улица Чехова, 22"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(chat_id='@shoraga_test', latitude="47°12′19″", longitude="38°56′23″")
   else:
      bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=markup_menu)

def get_schedule(day):
   schedule = []
   pair_list = []
   url = "http://ictib.host1809541.hostland.pro/index.php/api/get_day_schedule"
   params = dict(
      day=day,
      user_id='8745589874'
   )
   resp = requests.get(url=url, params=params)
   binary = resp.content
   data = json.loads(binary)
   for idx, pair in enumerate(data['pairs'], start=0):
      del pair_list[:]
      if pair['pair_name']:
         pair_list.append("Пара №{}: {} \n".format(idx+1, pair['time']))
         pair_list.append(pair['pair_name'] + '\n\n')
      else:
         pair_list.append("Пара №{}: Окно \n\n".format(idx+1))
      print(pair_list)
      schedule.append(pair_list[:])
      print(schedule)
   print(schedule)
   text = ''

   for schedules in schedule:
      text += '' + ''.join(schedules)
   
   text = "Дата - {}\nНеделя - {}\n\n{}".format(data['day'], data['week'], text)

   # data = json.dumps(data) 
   return text

def get_day_of_week(today):
   day = datetime.datetime.today().weekday()+1
   print(datetime.datetime.today())
   print(day)
   if not today:
      day += 1
   if day == 1:
      print('Пнд')
      return 'Пнд'
   elif day == 2:
      print('Втр')
      return 'Втр'
   elif day == 3:
      print('Срд')
      return 'Срд'
   elif day == 4:
      print('Чтв')
      return 'Чтв'
   elif day == 5:
      print('Птн')
      return 'Птн'   
   elif day == 6:
      print('Сбт')
      return 'Сбт' 
   else:
      print('undefined')
      return 'Пнд'

# SERVER SIDE 
@server.route('/' + config.token, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200
@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='https://infinite-waters-23955.herokuapp.com/' + TOKEN)
   return "!", 200
if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

   