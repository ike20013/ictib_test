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
markup_menu.row('Собственное расписание')
markup_menu.row('Информация о вузе')
markup_menu.row('Настройки')

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

markup_user_schedule = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_user_schedule.row('Удалить пару', 'Редактировать')
markup_user_schedule.row('Назад')

markup_user_schedule_day = types.InlineKeyboardMarkup(resize_keyboard=True)
markup_user_schedule_day.row('Пнд', 'Втр', 'Срд')
markup_user_schedule_day.row('Чтв', 'Птн', 'Сбт')

markup_user_schedule_pair_count = types.InlineKeyboardMarkup(resize_keyboard=True)
markup_user_schedule_pair_count.row('1', '2', '3')
markup_user_schedule_pair_count.row('4', '5', '6')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Добро пожаловать, введите группу (Пример КТбо2-3)")
    bot.register_next_step_handler(msg, reg_user)

def reg_user(message):
    url = "http://ictib.host1809541.hostland.pro/index.php/api/reg_user"
    print(message.text)
    params = dict(
       user_id=message.from_user.id,
       user_group=message.text
    )
    resp = requests.get(url=url, params=params)
    print(resp.content)
    binary = resp.content
    data = json.loads(binary)

    chat_id = message.chat.id

    if data['success'] == 'true':
        text = 'Все окей'
        bot.send_message(chat_id, text)
    elif data['success'] == 'false':
        msg = bot.reply_to(message, "Повтори")
        bot.register_next_step_handler(msg, reg_user)
    else:
        msg = bot.reply_to(message, "Ты уже есть")
        bot.register_next_step_handler(msg, reg_user)

@bot.message_handler(content_types=['text'])
def handle_text(message):
   global group
   if message.text == "1":
      bot.send_message(message.chat.id, "Ну и нахуя", reply_markup=markup_menu)
   elif message.text == "Расписание группы":
      get_week_schedule(message.from_user.id)
      bot.send_message(message.chat.id, "Выберите день", reply_markup=markup_schedule)
   elif message.text == "Информация о вузе":
      bot.send_message(message.chat.id, "Какая информация вам инетересна?", reply_markup=markup_info)
   elif message.text == "Информация о корпусах":
      bot.send_message(message.chat.id, "Выберете корпус", reply_markup=markup_corps)
   elif message.text == "Сегодня":
      day = get_day_of_week(True)
      text = get_schedule(day, message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Завтра":
      day = get_day_of_week(False)
      text = get_schedule(day, message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Понедельник":
      text = get_schedule('Пнд', message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Вторник":
      text = get_schedule('Втр', message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule) 
   elif message.text == "Среда":
      text = get_schedule('Срд', message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Четверг":
      text = get_schedule('Чтв', message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Пятница":
      text = get_schedule('Птн', message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Суббота":
      text = get_schedule('Сбт', message.from_user.id)
      bot.send_message(message.chat.id, text, reply_markup=markup_schedule)
   elif message.text == "Основные сайты":
      text = '\u25b6\ufe0f [Личный кабинет студента](https://sfedu.ru/www/stat_pages22.show?p=STD/lks/D)\n\u25b6\ufe0f [LMS](https://lms.sfedu.ru)\n\u25b6\ufe0f [БРС](https://grade.sfedu.ru/)\n\u25b6\ufe0f [Сайт ИКТИБа](http://ictis.sfedu.ru/)\n\u25b6\ufe0f [Проектный офис ИКТИБ](https://proictis.sfedu.ru/)'
      bot.send_message(message.chat.id, text, reply_markup=markup_info, parse_mode='MarkdownV2')
   elif message.text == "Группы Вконтакте":
      text = '\u27A1\ufe0f [Физическая культура в ИТА ЮФУ](https://vk.com/club101308251)\n\u27A1\ufe0f [Подслушано в ЮФУ](https://vk.com/overhearsfedu)\n\u27A1\ufe0f [ИКТИБ ЮФУ](https://vk.com/ictis_sfedu)\n\u27A1\ufe0f [Студенческий клуб ИТА ЮФУ \(г\. Таганрог\)](https://vk.com/studclub_tgn)\n\u27A1\ufe0f  [Студенческий киберспортивный клуб ЮФУ](https://vk.com/esports_sfedu)\n\u27A1\ufe0f [Культура здоровья в ИТА ЮФУ](https://vk.com/club150688847)\n\u27A1\ufe0f [Первокурснику](https://vk.com/1kurs_ita_2019)\n\u27A1\ufe0f [Технологии \+ Проекты \+ Инновации ИКТИБ](https://vk.com/proictis)\n\u27A1\ufe0f [Волонтерский центр ИКТИБ ЮФУ](https://vk.com/ictis_vol)'
      bot.send_message(message.chat.id, text, reply_markup=markup_info, parse_mode='MarkdownV2')
   elif message.text == "Корпус А":
      text = "Таганрог, улица Чехова, 22"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.205446", longitude="38.938832")
   elif message.text == "Корпус Б":
      text = "Таганрог, улица Чехова, 22"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.205396", longitude="38.938842")
   elif message.text == "Корпус В":
      text = "Таганрог, ул. Петровская, 81"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.216498", longitude="38.926859")
   elif message.text == "Корпус Г":
      text = "Таганрог, Некрасовский переулок, 42"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.203241", longitude="38.934853")
   elif message.text == "Корпус Д":
      text = "Таганрог, Некрасовский переулок, 44"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.205446", longitude="38.938832")
   elif message.text == "Корпус Е":
      text = "Таганрог, ул. Шевченко, 2"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.204446", longitude="38.944437")
   elif message.text == "Корпус И":
      text = "Таганрог, улица Чехова, 2"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.203932", longitude="38.943927")
   elif message.text == "Корпус К":
      text = "Таганрог, ул. Шевченко, 2"
      bot.send_message(message.chat.id, text, reply_markup=markup_corps)
      bot.send_location(message.chat.id, latitude="47.204446", longitude="38.944437")
   elif message.text == "Настройки":
      group = get_user_group(message.from_user.id)
      markup_config = types.ReplyKeyboardMarkup(resize_keyboard=True)
      markup_config.row("Группа: {}".format(group))
      markup_config.row("Назад")
      text = "Настройки"
      bot.send_message(message.chat.id, text, reply_markup=markup_config)
   elif message.text == "Группа: {}".format(group):
      msg = bot.send_message(message.chat.id, "Введите группу (Пример КТбо2-3)")
      bot.register_next_step_handler(msg, change_group)
   elif message.text == "Собственное расписание":
      bot.send_message(message.chat.id, "Выберите день", reply_markup=markup_user_schedule_day)
      if message.text == "Пнд":
         bot.send_message(message.chat.id, "Выберите пару", reply_markup=markup_user_schedule_pair_count)
   else:
      bot.send_message(message.chat.id, "Вы вернулись назад", reply_markup=markup_menu)

def change_group(message):
    url = "http://ictib.host1809541.hostland.pro/index.php/api/change_user_group"
    print(message.text)
    params = dict(
       user_id=message.from_user.id,
       user_group=message.text
    )
    resp = requests.get(url=url, params=params)
    print(resp.content)
    binary = resp.content
    data = json.loads(binary)

    chat_id = message.chat.id

    if data['success'] == 'true':
        global group
        text = 'Все окей'
        group = message.text
        markup_config = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_config.row("Группа: {}".format(group))
        markup_config.row("Назад")
        bot.send_message(chat_id, text, reply_markup=markup_config)
    elif data['success'] == 'false':
        msg = bot.reply_to(message, "Повтори")
        bot.register_next_step_handler(msg, change_group)
    else:
        msg = bot.reply_to(message, "Ты уже есть")
        bot.register_next_step_handler(msg, change_group)


def get_week_schedule(user_id):
    url = "http://ictib.host1809541.hostland.pro/index.php/api/get_week_schedule"
    params = dict(
        user_id=user_id
    )
    resp = requests.get(url=url, params=params)
    return resp.content

def get_schedule(day, user_id):
   schedule = []
   pair_list = []
   url = "http://ictib.host1809541.hostland.pro/index.php/api/get_day_schedule"
   params = dict(
      day=day,
      user_id=user_id
   )
   resp = requests.get(url=url, params=params)
   print(resp.content)
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

def get_user_group(user_id):
   url = "http://ictib.host1809541.hostland.pro/index.php/api/get_info"
   params = dict(
      user_id=user_id
   )
   resp = requests.get(url=url, params=params)
   binary = resp.content
   data = json.loads(binary)
   user_group = data['user_group']
   return user_group


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

if __name__ == '__main__':
    bot.polling(none_stop=True)