import os
import telebot
from telebot import types
from flask import Flask, request

TOKEN = '1271897314:AAG1c6rZ8JnGtRA2Mx1mJ1A7LOHCo_-ysVY'
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)
keyboard_main = types.ReplyKeyboardMarkup(True)
keyboard_schedule = types.ReplyKeyboardMarkup(True)

keyboard_main.row('Расписание группы')
keyboard_schedule.row('Сегодня', 'Завтра', 'Понедельник', 'Вторни', 'Среда', 'Четверг', 'Пятница', 'Суббота','Назад')


# Bot's Functionalities
def sendMessage(message, text):
   bot.send_message(message.chat.id, text)
# This method will send a message formatted in HTML to the user whenever it starts the bot with the /start command, feel free to add as many commands' handlers as you want
@bot.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Welcome to the Medium 🤖!</b>\n"
   "Say Hello to the bot to get a reply from it!"
   )
   bot.send_message(message.chat.id, text, reply_markup=keyboard_main, parse_mode='HTML')
# This method will fire whenever the bot receives a message from a user, it will check that there is actually a not empty string in it and, in this case, it will check if there is the 'hello' word in it, if so it will reply with the message we defined
@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
    if 'hello'in message.text.lower():
      sendMessage(message, 'Hello! How are you doing today?')
    elif 'я тебя люблю' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

# SERVER SIDE 
@server.route('/' + TOKEN, methods=['POST'])
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