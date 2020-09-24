# -*- coding: utf-8 -*-

import os
import telebot
from telebot import types
from flask import Flask, request
import config
import match
import requests
import json 

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
      text = get_schedule()
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   else:
      bot.send_message(message.chat.id, "....", reply_markup=markup_menu)

def get_schedule():
   schedule = []
   pair_list = []
   url = "http://ictib.host1809541.hostland.pro/index.php/api/get_day_schedule?day=Втр&user_id=8745589874"
   resp = requests.get(url=url)
   binary = resp.content
   data = json.loads(binary)
   for pair in data['pairs']:
      # pair_list.append(data['pairs'][pair]['pair_name'])
      # pair_list.append(data['pairs'][pair]['time'])
      # schedule.append(pair_list)
      print(pair)
      schedule.append(pair)
   # data = json.dumps(data)
   return "hello"

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