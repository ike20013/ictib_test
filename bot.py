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

markup_schedule = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_schedule.row('Сегодня', 'Завтра')
markup_schedule.row('Понедельник', 'Вторник', 'Среда')
markup_schedule.row('Четверг', 'Пятница', 'Суббота')
markup_schedule.row('Назад')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, введите группу (Пример КТбо2-3)", reply_markup = markup_menu)

@bot.message_handler(content_types=['text'])
def handle_text(message):
   if message.text == "1":
      bot.send_message(message.chat.id, "Ну и нахуя", reply_markup=markup_menu)
   elif message.text == "Расписание группы":
      bot.send_message(message.chat.id, "Выберите день", reply_markup=markup_schedule)
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
   else:
      bot.send_message(message.chat.id, "....", reply_markup=markup_menu)

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
   day = datetime.datetime.today().weekday()
   if today:
      continue
   else:
      day += 1
   if day == 1 or 8:
      return 'Пнд'
   if day == 2:
       return 'Втр'
   if day == 3:
       return 'Срд'
   if day == 4:
       return 'Чтв'
   if day == 5:
       return 'Птн'   
   if day == 6:
       return 'Сбт' 
   if day == 7:
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