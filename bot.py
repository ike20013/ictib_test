# -*- coding: utf-8 -*-

import os
import telebot
from telebot import types
from flask import Flask, request
import config
import match

bot = telebot.TeleBot(config.token)
server = Flask(__name__)


#bot.send_message(390728072, "test")

#upd = bot.get_updates()
#print(upd)
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

print(bot.get_me())

#, 254105252
vipid = [390728072, 568252309, 326258723, 512525666, 415666030, 408900121, 685497917]
premiumid = [390728072, 685497917]

keyboard = types.InlineKeyboardMarkup()

markup_vlosh = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_krip = types.KeyboardButton('Криптoвалюта')
btn_val =types.KeyboardButton('Рубли')
btn_back = types.KeyboardButton('\U0001F519Oбратно')
markup_vlosh.add(btn_krip, btn_val, btn_back)


markup_priobvip = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_qiwi = types.KeyboardButton('Qiwi')
btn_yandex = types.KeyboardButton('Yandex.Mоney')
btn_visa = types.KeyboardButton('Картoй')
btn_krip = types.KeyboardButton('Криптовалютa')
btn_back = types.KeyboardButton('\U0001F519Обратнo')
markup_priobvip.add(btn_qiwi, btn_yandex, btn_visa, btn_krip, btn_back)

markup_priobprem = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_qiwi = types.KeyboardButton('QIWI')
btn_yandex = types.KeyboardButton('Yandex.Money')
btn_visa = types.KeyboardButton('Картой')
btn_krip = types.KeyboardButton('Криптовалюта')
btn_back = types.KeyboardButton('\U0001F519Обратно')
markup_priobprem.add(btn_qiwi, btn_yandex, btn_visa, btn_krip, btn_back)


markup_priv = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_vip = types.KeyboardButton('VIP')
btn_prem = types.KeyboardButton('Premium')
btn_back = types.KeyboardButton('\U0001F519Назад')
markup_priv.add(btn_vip, btn_prem, btn_back)

markup_prem = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_pay = types.KeyboardButton('Приобрести Premium')
btn_info = types.KeyboardButton('\u2753Информация о Premium\u2753')
btn_check = types.KeyboardButton('Проверить статус Premium')
btn_back = types.KeyboardButton('\U0001F519Нaзaд')
markup_prem.add(btn_pay, btn_info ,btn_check, btn_back)


markup_sklad = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_pay1 = types.KeyboardButton('Вложиться')
btn_info1 = types.KeyboardButton('\u2753Информация о складчине\u2753')
btn_question = types.KeyboardButton('Задать вопрос')
btn_back = types.KeyboardButton('\U0001F519Нaзад')
markup_sklad.add(btn_pay1, btn_question, btn_info1 , btn_back)

markup_vip = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
btn_pay = types.KeyboardButton('Приобрести VIP')
btn_info = types.KeyboardButton('\u2753Информация о VIP\u2753')
btn_check = types.KeyboardButton('Проверить статус VIP')
btn_back = types.KeyboardButton('\U0001F519Нaзaд')
markup_vip.add(btn_pay, btn_info ,btn_check, btn_back)


markup_dop = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btn_eks = types.KeyboardButton('Экспрессы')
btn_inf = types.KeyboardButton('\u2753Информация\u2753')
btn_day = types.KeyboardButton('Ставка дня')
btn_sklad = types.KeyboardButton('Складчина')
btn_back = types.KeyboardButton('\U0001F519Назад')
markup_dop.add(btn_eks, btn_day , btn_sklad, btn_inf, btn_back)


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btn_sport = types.KeyboardButton('\u26BDВид спорта\u26BD')
btn_chm = types.KeyboardButton('\U0001F3C6ЧМ\U0001F3C6')
btn_exit = types.KeyboardButton('\U0001F911Доп. услуги\U0001F911')
btn_vip = types.KeyboardButton('\U0001F451Привилегии\U0001F451')
#btn_live = types.KeyboardButton('\U0001F534Лайв\U0001F534')
btn_live = types.KeyboardButton('\u2753Вопрос\u2753')

markup_menu.add(btn_sport, btn_chm, btn_exit, btn_live, btn_vip)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup = markup_menu)

markup_sport = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btn_foot = types.KeyboardButton('\u26BDФутбол')
btn_tennis = types.KeyboardButton('\U0001F3BEТеннис')
btn_baseball = types.KeyboardButton('\u26BEБейсбол')
btn_basket = types.KeyboardButton('\U0001F3C0Баскетбол')
btn_back = types.KeyboardButton('\U0001F519Назад')
markup_sport.add(btn_foot, btn_tennis, btn_baseball, btn_basket, btn_back)


#321235833

@bot.message_handler(content_types=['text'])
def handle_text(message):
    a = 0
    b = 0
    for item in vipid:
        if int(message.from_user.id) == int(item):
            a += 1
        elif int(message.from_user.id) != int(item):
            a += 0
    for item1 in premiumid:
        if int(message.from_user.id) == int(item1):
            b += 1
        if int(message.from_user.id) != int(item1):
            b += 0
    if message.text == "1":
        bot.send_message(message.chat.id, "....", reply_markup=markup_menu)
    elif message.text == "\u26BDВид спорта\u26BD":
        bot.send_message(message.chat.id, "Выберите спорт\n", reply_markup=markup_sport)
    elif message.text == "Проверить статус VIP":
        if a == 0:
            bot.send_message(message.chat.id, "Ваш статус VIP:Не активен", reply_markup=markup_vip)
        elif b == 1:
            bot.send_message(message.chat.id, "Вам доступны все привилегии VIP\nт.к имеется статус Premium", reply_markup=markup_vip)
        elif a == 1:
            bot.send_message(message.chat.id, "Ваш статус VIP:Активен", reply_markup=markup_vip)
    elif message.text == "\U0001F911Доп. услуги\U0001F911":
        bot.send_message(message.chat.id, "Выберите дополнительную услугу", reply_markup=markup_dop)
    elif message.text == "\U0001F451Привилегии\U0001F451":
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup_priv)
    elif message.text == "VIP":
        bot.send_message(message.chat.id, "VIP", reply_markup=markup_vip)
    elif message.text == "Premium":
        bot.send_message(message.chat.id, "Premium", reply_markup=markup_prem)
    elif message.text == "Приобрести Premium":
        if b == 1:
         bot.send_message(message.chat.id, "У вас уже имеется данная Привилегия", reply_markup=markup_prem)
        else:
         bot.send_message(message.chat.id,"Выберите способ оплаты",reply_markup=markup_priobprem)
    elif message.text == "\u2753Информация о Premium\u2753":
        bot.send_message(message.chat.id, match.prem_infa, reply_markup=markup_prem)
    elif message.text == "Проверить статус Premium":
        if b == 1:
            bot.send_message(message.chat.id, "Ваш статус Premium:Активен", reply_markup=markup_prem)
        else:
            bot.send_message(message.chat.id, "Ваш статус Premium:Не активен", reply_markup=markup_prem)
    elif message.text == "\U0001F519Нaзaд":
        bot.send_message(message.chat.id, "Выберите что вас интересует", reply_markup=markup_priv)
    elif message.text == "\u2753Информация о VIP\u2753":
        bot.send_message(message.chat.id, match.vip_infa, reply_markup=markup_vip)
    elif message.text == "Приобрести VIP":
        if a == 0:
         bot.send_message(message.chat.id, "Выберите способ оплаты", reply_markup=markup_priobvip)
        elif b == 1:
            bot.send_message(message.chat.id,"У вас есть полный доступ к VIP Привилегиям\nт.к у вас Premium", reply_markup=markup_vip)
        elif a == 1:
            bot.send_message(message.chat.id,"У вас уже имеется данная Привилегия", reply_markup=markup_vip)
    elif message.text == "Складчина":
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=markup_sklad)
    elif message.text == "\U0001F519Назад":
        bot.send_message(message.chat.id, "Выберите услугу", reply_markup=markup_menu)
    elif message.text == "\U0001F519Нaзад":
        bot.send_message(message.chat.id, "Выберите услугу", reply_markup=markup_dop)
    elif message.text == "\u26BDФутбол":
            if match.football == "" and match.vip_foot == "":
                 bot.send_message(message.chat.id, match.none, reply_markup=markup_sport)
            elif match.football != "" and match.vip_foot != "":
                if a == 1:
                    bot.send_message(message.chat.id, match.football, reply_markup=markup_sport)
                    bot.send_message(message.chat.id, match.vip_foot, reply_markup=markup_sport)
                elif a == 0:
                    bot.send_message(message.chat.id, match.football, reply_markup=markup_sport)
                    keyboard = types.InlineKeyboardMarkup()
                    callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP2")
                    keyboard.add(callback_button)
                    bot.send_message(message.chat.id, match.infvip2, reply_markup=keyboard)
            elif match.football != "":
                bot.send_message(message.chat.id, match.football, reply_markup=markup_sport)
                for item in vipid:
                    if int(message.from_user.id) == int(item):
                        bot.send_message(message.chat.id, match.vip_foot, reply_markup=markup_sport)
            elif match.football == "" and match.vip_foot != "":
                if a == 1:
                    bot.send_message(message.chat.id, match.vip_foot, reply_markup=markup_sport)
                elif a == 0:
                    keyboard = types.InlineKeyboardMarkup()
                    callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP")
                    keyboard.add(callback_button)
                    bot.send_message(message.chat.id, match.infvip, reply_markup=keyboard)
                    bot.send_message(message.chat.id, "Главное меню", reply_markup=markup_menu)
    elif message.text == "\U0001F3BEТеннис":
        if match.tenn == "" and match.vip_tenn == "":
            bot.send_message(message.chat.id, match.none, reply_markup=markup_sport)
        elif match.tenn != "" and match.vip_tenn != "":
            if a == 1:
                bot.send_message(message.chat.id, match.tenn, reply_markup=markup_sport)
                bot.send_message(message.chat.id, match.vip_tenn, reply_markup=markup_sport)
            elif a == 0:
                bot.send_message(message.chat.id, match.tenn, reply_markup=markup_sport)
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP2")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip2, reply_markup=keyboard)
        elif match.tenn != "":
            bot.send_message(message.chat.id, match.tenn, reply_markup=markup_sport)
            for item in vipid:
                if int(message.from_user.id) == int(item):
                    bot.send_message(message.chat.id, match.vip_tenn, reply_markup=markup_sport)
        elif match.tenn == "" and match.vip_tenn != "":
            if a == 1:
                bot.send_message(message.chat.id, match.vip_tenn, reply_markup=markup_sport)
            elif a == 0:
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip, reply_markup=keyboard)
                bot.send_message(message.chat.id, "Главное меню", reply_markup=markup_menu)
    elif message.text == "\u26BEБейсбол":
        if match.base == "" and match.vip_base == "":
            bot.send_message(message.chat.id, match.none, reply_markup=markup_sport)
        elif match.base != "" and match.vip_base != "":
            if a == 1:
                bot.send_message(message.chat.id, match.base, reply_markup=markup_sport)
                bot.send_message(message.chat.id, match.vip_base, reply_markup=markup_sport)
            elif a == 0:
                bot.send_message(message.chat.id, match.base, reply_markup=markup_sport)
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP2")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip2, reply_markup=keyboard)
        elif match.base != "":
            bot.send_message(message.chat.id, match.base, reply_markup=markup_sport)
            for item in vipid:
                if int(message.from_user.id) == int(item):
                    bot.send_message(message.chat.id, match.vip_base, reply_markup=markup_sport)
        elif match.base == "" and match.vip_base != "":
            if a == 1:
                bot.send_message(message.chat.id, match.vip_base, reply_markup=markup_sport)
            elif a == 0:
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip, reply_markup=keyboard)
                bot.send_message(message.chat.id, "Главное меню", reply_markup=markup_menu)
    elif message.text == "\U0001F3C0Баскетбол":
        if match.basket == "" and match.vip_basket == "":
            bot.send_message(message.chat.id, match.none, reply_markup=markup_sport)
        elif match.basket != "" and match.vip_basket != "":
            if a == 1:
                bot.send_message(message.chat.id, match.basket, reply_markup=markup_sport)
                bot.send_message(message.chat.id, match.vip_basket, reply_markup=markup_sport)
            elif a == 0:
                bot.send_message(message.chat.id, match.basket, reply_markup=markup_sport)
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP2")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip2, reply_markup=keyboard)
        elif match.basket != "":
            bot.send_message(message.chat.id, match.basket, reply_markup=markup_sport)
            for item in vipid:
                if int(message.from_user.id) == int(item):
                    bot.send_message(message.chat.id, match.vip_basket, reply_markup=markup_sport)
        elif match.basket == "" and match.vip_basket != "":
            if a == 1:
                bot.send_message(message.chat.id, match.vip_basket, reply_markup=markup_sport)
            elif a == 0:
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip, reply_markup=keyboard)
                bot.send_message(message.chat.id, "Главное меню", reply_markup=markup_menu)
    elif message.text == "\U0001F3C6ЧМ\U0001F3C6":
        if match.chm1 == "" and match.vip_chm == "":
            bot.send_message(message.chat.id, match.none, reply_markup=markup_menu)
        elif match.chm1 != "" and match.vip_chm != "":
            if a == 1:
                bot.send_message(message.chat.id, match.chm1, reply_markup=markup_menu)
                bot.send_message(message.chat.id, match.vip_chm, reply_markup=markup_menu)
            elif a == 0:
                bot.send_message(message.chat.id, match.chm1, reply_markup=markup_menu)
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip2, reply_markup=keyboard)
        elif match.chm1 != "":
            bot.send_message(message.chat.id, match.chm1, reply_markup=markup_menu)
            for item in vipid:
                if int(message.from_user.id) == int(item):
                    bot.send_message(message.chat.id, match.vip_chm, reply_markup=markup_menu)
        elif match.chm1 == "" and match.vip_chm != "":
            if a == 1:
                bot.send_message(message.chat.id, match.vip_chm, reply_markup=markup_menu)
            elif a == 0:
                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="\u2753Как приобрести Привилегии\u2753", callback_data="VIP")
                keyboard.add(callback_button)
                bot.send_message(message.chat.id, match.infvip, reply_markup=keyboard)
                bot.send_message(message.chat.id, "Главное меню", reply_markup=markup_menu)
    elif message.text == "\U0001F534Лайв\U0001F534":
        bot.send_message(message.chat.id, match.live, reply_markup=markup_menu)
    elif message.text == "\u2753Информация\u2753":
        if a == 0:
            bot.send_message(message.chat.id, match.info_without_vip, reply_markup=markup_dop)
        elif b == 1:
            bot.send_message(message.chat.id, match.info_with_prem, reply_markup=markup_dop)
        elif a == 1:
            bot.send_message(message.chat.id, match.info_with_vip, reply_markup=markup_dop)
    elif message.text == "Экспрессы":
        if b == 1:
            bot.send_message(message.chat.id, match.vip_ex, reply_markup=markup_dop)
        else:
            bot.send_message(message.chat.id, match.ex_inf, reply_markup=markup_dop)
    elif message.text == "Ставка дня":
        if b == 1:
            bot.send_message(message.chat.id, match.shb, reply_markup=markup_dop)
        else:
            bot.send_message(message.chat.id, match.shb_info, reply_markup=markup_dop)
    elif message.text == "Вложиться":
        bot.send_message(message.chat.id, "Выберите способ вложения", reply_markup=markup_vlosh)
    elif message.text == "\u2753Информация о складчине\u2753":
        bot.send_message(message.chat.id, match.sklad_info, reply_markup=markup_sklad)
    elif message.text == "QIWI":
        bot.send_message(message.chat.id, match.qiwi_prem, reply_markup=markup_priobprem)
    elif message.text == "Qiwi":
        bot.send_message(message.chat.id, match.qiwi_vip, reply_markup=markup_priobvip)
    elif message.text == "Yandex.Money":
        bot.send_message(message.chat.id, match.yandex_prem, reply_markup=markup_priobprem)
    elif message.text == "Картой":
        bot.send_message(message.chat.id, match.karta_prem, reply_markup=markup_priobprem)
    elif message.text == "Криптовалюта":
        bot.send_message(message.chat.id, match.kripta_prem, reply_markup=markup_priobprem)
    elif message.text == "Yandex.Mоney":
        bot.send_message(message.chat.id, match.yandex_vip, reply_markup=markup_priobvip)
    elif message.text == "Картoй":
        bot.send_message(message.chat.id, match.karta_vip, reply_markup=markup_priobvip)
    elif message.text == "Криптовалютa": #последняя а
        bot.send_message(message.chat.id, match.kripta_vip, reply_markup=markup_priobvip)
    elif message.text == "\U0001F519Обратно":
        bot.send_message(message.chat.id, "Premium", reply_markup=markup_prem)
    elif message.text == "\U0001F519Обратнo":
        bot.send_message(message.chat.id, "VIP", reply_markup=markup_vip)
    elif message.text == "Криптoвалюта":
        bot.send_message(message.chat.id, match.vlosh_krip, reply_markup=markup_vlosh)
    elif message.text == "Рубли":
        bot.send_message(message.chat.id, match.vlosh_val, reply_markup=markup_vlosh)
    elif message.text == "\U0001F519Oбратно":
        bot.send_message(message.chat.id, "Складчина", reply_markup=markup_sklad)
    elif message.text == "Задать вопрос":
        bot.send_message(message.chat.id, "По всем вопросам о складчине - @telecap_support2", reply_markup=markup_sklad)
    elif message.text == "\u2753Вопрос\u2753":
        bot.send_message(message.chat.id, "По всем вопросам - @telecap_support \n И @telecap_support2", reply_markup=markup_menu)
    else:
        bot.send_message(message.chat.id, "....", reply_markup=markup_menu)
		
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "VIP":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что бы приобрести Привилегии, вам надо нажать соответствующую кнопку, она в самом низу")
        if call.data == "VIP2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что бы приобрести Привилегии, нажмите Назад "
                                                                                                         "и найдите соответствующую вкладку, она в самом низу, затем нажмите на неё")
"""
@bot.message_handler(content_types=['text'])
def handle_text(message):
    a = 0
    for item in vipid:
        if int(message.from_user.id) == int(item):
            a += 1
        elif int(message.from_user.id) != int(item):
            a += 0
"""


bot.polling(none_stop=True, interval=0)

"""
def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id,"я безграничен, человек")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты не умеешь играть"
    if message.text == "а":
        answer = "Б"
        log(message, answer)
        bot.send_message(message.chat.id, "Б")
    elif message.text == "б":
        answer = "В"
        bot.send_message(message.chat.id, "В")
        log(message, answer)
    elif message.text == "1" or message.text == "2":
        answer = "Это 1 или 2, я уверен"
        bot.send_message(message.chat.id, "Это 1 или 2, я уверен")
        log(message, answer)
    elif message.text == "?" and str(message.from_user.id) == "390728072":
        answer = "Ты избранный!!!!"
        bot.send_message(message.chat.id, "Ты избранный!!!!")
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


"""
"""
@bot.message_handler(commands=['start1'])
def handle_start(message):
    sport_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    sport_markup.row('Футбол', 'Теннис')
    sport_markup.row('Бейсбол', 'Баскетбол')
    bot.send_message(message.from_user.id, 'Выберите желаемый спорт', reply_markup=sport_markup)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(u'\u26BD Вид спорта',u'\U0001F3C6 ЧМ')
    user_markup.row('Выход','Купить ВИП','ЛАЙВ')
    bot.send_message(message.from_user.id, 'Добро пожаловать..',reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Live атчи можно увидеть на нашем канале, вступай быстрее !!! -> Ссылка"
    if message.text == "ЛАЙВ":
        bot.send_message(message.chat.id, "Live атчи можно увидеть на нашем канале, вступай быстрее !!! -> Ссылка")

"""

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