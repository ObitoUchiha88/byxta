#-*- coding: utf-8 -*-
import telebot
import os
import requests
from telebot import types

import random
import py_key

bot = telebot.TeleBot(py_key.token)
#bot.send_message(466835416, "test")
upd = bot.get_updates()
#print(upd)
print(bot.get_me())

a = 42
b = "qwerty"
age = 0
phone = 0
number = 0
age1 = 0
phone1 = 0
number1 = 0
age2 = 0
phone2 = 0
number2 = 0
age3 = 0
phone3 = 0
number3 = 0
age4 = 0
phone4 = 0
number4 = 0

print(type(a), type(b))






@bot.message_handler(commands=['start']) #Запуск бота
def start_command(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    kno1 = types.InlineKeyboardButton(text="Оформить заказ\U0001F4DD", callback_data="1")
    kno3 = types.InlineKeyboardButton(text="Связь с оператором\U0001F4DE", url="https://t.me/DExpressBro")
    keyboardmain.add(kno1)
    keyboardmain.add(kno3)

    bot.send_message(message.chat.id, """\r    
    \U0001F4E8*DrugExpress* _приветствует тебя
                        мой друг_ \U0001F44B
                        
    
    \U0001F4CD*Это бот для автооформления заказа
    на отправления посылок по Украине*\U0001F4EC
    
    `\U0001F69B Доставка осущиствляеться 
     почтовыми службами \U0001F3E4
     в течении 1-3 рабочих дней \U0001F551`
     
    
    \U0001F4CD`полностью` *анонимное*\U0001F464 `сотрудничество` \U0001F91D
    
    \U0001F449 *ОПТ* от *50г* \U0001F4A5
    
    \U0001F449 *Минимальная сумма заказа* *500грн* \U0001F4B5
    
    \U0001F5B1 Нажмите `[`*Оформить заказ*`]` для выбора 
                        и заказа товара \U0001F6CD
    
    """, parse_mode="Markdown", reply_markup=keyboardmain)



@bot.callback_query_handler(func=lambda call: call.data == "1")
def callback_inline(call):
    if call.data == "1":
        keyboard = types.InlineKeyboardMarkup()
        kno1 = types.InlineKeyboardButton(text = "\U0001F449 Шишки", callback_data = "1.1")
        kno3 = types.InlineKeyboardButton(text = "\U0001F449 Амфетамин", callback_data = "2.1")
        kno4 = types.InlineKeyboardButton(text = "\U0001F449 Альфа-PVP", callback_data = "3.1")
        kno5 = types.InlineKeyboardButton(text = "\U0001F449 MDMA", callback_data = "4.1")
        kno2 = types.InlineKeyboardButton(text = "\U0001F449 XTC", callback_data = "5.1")
        keyboard.add(kno5)
        keyboard.add(kno1, kno3)
        keyboard.add(kno2, kno4)
        bot.send_message(chat_id=call.message.chat.id, text="""\r
                       \U0001F58B`Оформление Заказа`\U0001F58B
                       
           *Магазин DrugExpress гарантирует:
            
            \U0001F5A4 Высокое качество товара \U0001F680\U0001F4A5
            
            \U0001F5A4 Низкую цену товара \U0001F4B0\U0001F44D
            
            \U0001F5A4 Отличную упаковку товара \U0001F4E6\U0001F44D
            
            \U0001F5A4 Безопасное получение товара \U0001F464\U0001F4EC
            
            \U0001F4E8 Доставка осуществляется по всей Украине \U0001F30D
             \U0001F4E8   (`MeestExpress`, `IH-Тайм`, `Новая Почта`)* \U0001F4E5
           \U0001F48A *ТОВАР БУДЕТ НАДЁЖНО ЗАМАСКЕРОВАН ПОД НЕ ПРИМЕТНУЮ ПОСЫЛКУ* \U0001F9F8
           \U0001F4CD *К обычной стоимосте товара добавляеться* `50`*грн за упаковку*
            
            
           \U0001F5B1 Для продолжения заказа выбери товар \U0001F447""", parse_mode="Markdown", reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: call.data == "1.1")
def callback_next(call):
    if call.data == "1.1":
        bot.send_photo(chat_id = call.message.chat.id, photo = 'https://imbt.ga/BvBdehG7mB', caption = """\r
        *DrugExpress *

    \U0001F6CD * Товар: *Шишки 1г = 150грн

    \U0001F3D9 * Город: *

    \U0001F4E8 * Почта: *

    \U0001F464 * ФИО: *

    \U0001F4DE * Тел. *

    \U0001F3E4 * Отделение: *

    *Напиши город
    В который нужна доставка * """, parse_mode="Markdown")


    bot.register_next_step_handler(call.message, get_name)

def get_name(message):
    key = types.ReplyKeyboardMarkup(True, True)
    global name
    name = message.text
    key.row("MeestExpress", "IH-Тайм", "Новая Почта")
    bot.send_message(message.from_user.id, """\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Шишки 1г = 150грн

    \U0001F3D9*Город:* """+ name +"""

    \U0001F4E8*Почта:*""""""

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Выбери службу доставки*""", parse_mode = "Markdown", reply_markup = key )
    bot.register_next_step_handler(message, get_post)

def get_post(message):
    global post
    post = message.text
    bot.send_message(message.from_user.id, """\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Шишки 1г = 150грн

    \U0001F3D9*Город:* """+ name +"""

    \U0001F4E8*Почта:* """+ post +"""

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи данные для получения
    (Фамилию и инициалы)*""", parse_mode = "Markdown")
    bot.register_next_step_handler(message, get_finish)

def get_finish(message):
    global finish
    finish = message.text
    bot.send_message(message.from_user.id, """\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Шишки 1г = 150грн

    \U0001F3D9*Город:* """+ name +"""

    \U0001F4E8*Почта:* """+ post +"""

    \U0001F464*ФИО:* """+ finish +"""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи свой номер телефона
    (Только цыфрами начиная с 0)*""", parse_mode = "Markdown")
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Цыфрами")
    bot.send_message(message.from_user.id, """\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Шишки 1г = 150грн

    \U0001F3D9*Город:* """+ name +"""

    \U0001F4E8*Почта:* """+ post +"""

    \U0001F464*ФИО:* """+ finish +"""

    \U0001F4DE*Тел.* """+ str(age) + """

    \U0001F3E4*Отделение:*""""""

    *Введи почтовое отделение
    (Только цыфрами)*""", parse_mode = "Markdown")
    bot.register_next_step_handler(message, get_number)

def get_number(message):
    global number
    while number == 0:
        try:
            number = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, """\r *Цыфрами*""", parse_mode = "Markdown")
    bot.send_message(message.from_user.id, """\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Шишки 1г = 150грн

    \U0001F3D9*Город:* """+ name +"""

    \U0001F4E8*Почта:* """+ post +"""

    \U0001F464*ФИО:* """+ finish +"""

    \U0001F4DE*Тел.* """+ str(age) + """

    \U0001F3E4*Отделение:* """ + str(number) + """

    *Введи количество которое тебе нужно
    (Только цыфрами)*""", parse_mode = "Markdown")
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    keyboard1 = types.InlineKeyboardMarkup()
    global phone
    while phone == 0:
        try:
            phone = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Здесь используются только цифры" )
    kno = types.InlineKeyboardButton(text = "Связь с оператором\U0001F4DE" ,url = "https://t.me/DExpressBro" )
    kno1 = types.InlineKeyboardButton(text = "Выбор товара", callback_data = "1")
    keyboard1.add(kno)
    keyboard1.add(kno1)
    bot.send_message(message.from_user.id, """\r
                      *DrugExpress*
        `Товаро Транспортная Накладная\U0001F4DD`
       \U0001F194 """+str(random.randint(100000, 200000))+"""
        
    \U0001F6CD*Товар:* Шишки 1г = 150грн
    \U0001F3D9*Город:* """+ name +"""
    \U0001F4E8*Почта:* """+ post +"""
    \U0001F464*ФИО:* """+ finish +"""
    \U0001F4DE*Тел.* """+ str(age) + """
    \U0001F3E4*Отделение:* """ + str(number) + """
    
    \U0001F4B0*Сумма:* """+str(phone*150+50)+"""*грн*
     
    *Данные для отправки есть 
                Осталось оплатить заказ*
 `(`*Оплачивать нужно с рассчётом комиссии*`)`
                         
    \U0001F4B3`EasyPay` *- 66333880*
            
    *Сделай скрин оплаты \U0001F4F2
    \U0001F4E9 перешли это сообщение оператору* \U0001F464
    
    /start \U0001F449 Нажми и попадёшь в главное меню
    
    _Спасибо что выбрал наш сервис_ *DrugExpress*""", parse_mode="Markdown", reply_markup = keyboard1)


@bot.callback_query_handler(func = lambda call: call.data == "2.1")
def callback_step(call):
    if call.data == "2.1":
        bot.send_photo(chat_id = call.message.chat.id, photo='https://imbt.ga/nUpCHsYDz7', caption = """\r
                      *DrugExpress*

        \U0001F6CD*Товар:* Амфетамин 1г = 300грн

        \U0001F3D9*Город:*

        \U0001F4E8*Почта:*

        \U0001F464*ФИО:*

        \U0001F4DE*Тел.*

        \U0001F3E4*Отделение:*

        *Напиши город 
        В который нужна доставка*""", parse_mode = "Markdown" )
    bot.register_next_step_handler ( call.message, get_name1 )


def get_name1(message):
    key = types.ReplyKeyboardMarkup ( True ,True )
    global name1
    name1 = message.text
    key.row ( "MeestExpress" ,"IH-Тайм" ,"Новая Почта" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Амфетамин 1г = 150грн

    \U0001F3D9*Город:* """ + name1 + """

    \U0001F4E8*Почта:*""""""

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Выбери службу доставки*""" ,parse_mode = "Markdown" ,reply_markup = key )
    bot.register_next_step_handler ( message ,get_post1 )


def get_post1(message):
    global post1
    post1 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Амфетамин 1г = 300грн

    \U0001F3D9*Город:* """ + name1 + """

    \U0001F4E8*Почта:* """ + post1 + """

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи данные для получения
    (Фамилию и инициалы)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_finish1 )


def get_finish1(message):
    global finish1
    finish1 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Амфетамин 1г = 300грн

    \U0001F3D9*Город:* """ + name1 + """

    \U0001F4E8*Почта:* """ + post1 + """

    \U0001F464*ФИО:* """ + finish1 + """

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи свой номер телефона
    (Только цыфрами начиная с 0)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_age1 )


def get_age1(message):
    global age1
    while age1 == 0:
        try:
            age1 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Цыфрами" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Амфетамин 1г = 300грн

    \U0001F3D9*Город:* """ + name1 + """

    \U0001F4E8*Почта:* """ + post1 + """

    \U0001F464*ФИО:* """ + finish1 + """

    \U0001F4DE*Тел.* """ + str ( age1 ) + """

    \U0001F3E4*Отделение:*""""""

    *Введи почтовое отделение
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_number1 )


def get_number1(message):
    global number1
    while number1 == 0:
        try:
            number1 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"""\r *Цыфрами*""" ,parse_mode = "Markdown" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Амфетамин 1г = 300грн

    \U0001F3D9*Город:* """ + name1 + """

    \U0001F4E8*Почта:* """ + post1 + """

    \U0001F464*ФИО:* """ + finish1 + """

    \U0001F4DE*Тел.* """ + str ( age1 ) + """

    \U0001F3E4*Отделение:* """ + str ( number1 ) + """

    *Введи количество которое тебе нужно
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_phone1 )


def get_phone1(message):
    keyboard1 = telebot.types.InlineKeyboardMarkup ( )
    global phone1
    while phone1 == 0:
        try:
            phone1 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Здесь используются только цифры" )
    kno = types.InlineKeyboardButton ( text = "Связь с оператором\U0001F4DE" ,url = "https://t.me/DExpressBro" )
    kno1 = types.InlineKeyboardButton(text = "Выыбор товара", callback_data = "1")
    keyboard1.add (kno)
    keyboard1.add (kno1)

    bot.send_message ( message.from_user.id ,"""\r
                      *DrugExpress*
        `Товаро Транспортная Накладная` \U0001F4DD
       \U0001F194 """ + str ( random.randint ( 100000 ,200000 ) ) + """

    \U0001F6CD*Товар:* Амфетамин 1г = 300грн
    \U0001F3D9*Город:* """+ name1 +"""
    \U0001F4E8*Почта:* """+ post1 +"""
    \U0001F464*ФИО:* """+ finish1 +"""
    \U0001F4DE*Тел.* """+ str(age1) + """
    \U0001F3E4*Отделение:* """ + str(number1) + """
    
    \U0001F4B0*Сумма:* """+str(phone1*300+50)+"""*грн*
     
    *Данные для отправки есть 
                Осталось оплатить заказ*
 `(`*Оплачивать нужно с рассчётом комиссии*`)`
                         
    \U0001F4B3`EasyPay` *- 66333880*
            
    *Сделай скрин оплаты \U0001F4F2
    \U0001F4E9 перешли это сообщение оператору* \U0001F464
    
    /start \U0001F449 Нажми и попадёшь в главное меню
    
    _Спасибо что выбрал наш сервис_ *DrugExpress*""", parse_mode="Markdown", reply_markup = keyboard1)

@bot.callback_query_handler ( func = lambda call: call.data == "3.1" )
def callback_next(call):
    if call.data == "3.1":
        bot.send_photo ( chat_id = call.message.chat.id, photo='https://imbt.ga/EEUaiiyOvM', caption = """\r
                      *DrugExpress*

        \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн

        \U0001F3D9*Город:*

        \U0001F4E8*Почта:*

        \U0001F464*ФИО:*

        \U0001F4DE*Тел.*

        \U0001F3E4*Отделение:*

        *Напиши город 
        В который нужна доставка*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( call.message ,get_name2 )


def get_name2(message):
    key = types.ReplyKeyboardMarkup ( True ,True )
    global name2
    name2 = message.text
    key.row ( "MeestExpress" ,"IH-Тайм" ,"Новая Почта" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн

    \U0001F3D9*Город:* """ + name2 + """

    \U0001F4E8*Почта:*""""""

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Выбери службу доставки*""" ,parse_mode = "Markdown" ,reply_markup = key )
    bot.register_next_step_handler ( message ,get_post2 )


def get_post2(message):
    global post2
    post2 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн

    \U0001F3D9*Город:* """ + name2 + """

    \U0001F4E8*Почта:* """ + post2 + """

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи данные для получения
    (Фамилию и инициалы)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_finish2 )


def get_finish2(message):
    global finish2
    finish2 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн

    \U0001F3D9*Город:* """ + name2 + """

    \U0001F4E8*Почта:* """ + post2 + """

    \U0001F464*ФИО:* """ + finish2 + """

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи свой номер телефона
    (Только цыфрами начиная с 0)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_age2 )


def get_age2(message):
    global age2
    while age2 == 0:
        try:
            age2 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Цыфрами" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн

    \U0001F3D9*Город:* """ + name2 + """

    \U0001F4E8*Почта:* """ + post2 + """

    \U0001F464*ФИО:* """ + finish2 + """

    \U0001F4DE*Тел.* """ + str ( age2 ) + """

    \U0001F3E4*Отделение:*""""""

    *Введи почтовое отделение
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_number2 )


def get_number2(message):
    global number2
    while number2 == 0:
        try:
            number2 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"""\r *Цыфрами*""" ,parse_mode = "Markdown" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн

    \U0001F3D9*Город:* """ + name2 + """

    \U0001F4E8*Почта:* """ + post2 + """

    \U0001F464*ФИО:* """ + finish2 + """

    \U0001F4DE*Тел.* """ + str ( age2 ) + """

    \U0001F3E4*Отделение:* """ + str ( number2 ) + """

    *Введи количество которое тебе нужно
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_phone2 )


def get_phone2(message):
    keyboard1 = telebot.types.InlineKeyboardMarkup ( )
    global phone2
    while phone2 == 0:
        try:
            phone2 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Здесь используются только цифры" )
    kno = types.InlineKeyboardButton ( text = "Связь с оператором\U0001F4DE" ,url = "https://t.me/DExpressBro" )
    kno1 = types.InlineKeyboardButton ( text = "Выбор товара" , callback_data = "1")
    keyboard1.add ( kno )
    keyboard1.add ( kno1 )
    bot.send_message ( message.from_user.id ,"""\r
                      *DrugExpress*
        `Товаро Транспортная Накладная` \U0001F4DD
       \U0001F194 """ + str ( random.randint ( 100000 ,200000 ) ) + """

    \U0001F6CD*Товар:* Альфа-PVP 1г = 460грн
    \U0001F3D9*Город:* """+ name2 +"""
    \U0001F4E8*Почта:* """+ post2 +"""
    \U0001F464*ФИО:* """+ finish2 +"""
    \U0001F4DE*Тел.* """+ str(age2) + """
    \U0001F3E4*Отделение:* """ + str(number2) + """
    
    \U0001F4B0*Сумма:* """+str(phone2*460+50)+"""*грн*
     
    *Данные для отправки есть 
                Осталось оплатить заказ*
 `(`*Оплачивать нужно с рассчётом комиссии*`)`
                         
    \U0001F4B3`EasyPay` *- 66333880*
            
    *Сделай скрин оплаты \U0001F4F2
    \U0001F4E9 перешли это сообщение оператору* \U0001F464
    
    /start \U0001F449 Нажми и попадёшь в главное меню
    
    _Спасибо что выбрал наш сервис_ *DrugExpress*""", parse_mode="Markdown", reply_markup = keyboard1)


@bot.callback_query_handler ( func = lambda call: call.data == "4.1" )
def callback_next(call):
    if call.data == "4.1":
        bot.send_photo ( chat_id = call.message.chat.id, photo='https://imbt.ga/TLTkYqIAay', caption = """\r
                      *DrugExpress*

        \U0001F6CD*Товар:* MDMA 1г = 900грн

        \U0001F3D9*Город:*

        \U0001F4E8*Почта:*

        \U0001F464*ФИО:*

        \U0001F4DE*Тел.*

        \U0001F3E4*Отделение:*

        *Напиши город 
        В который нужна доставка*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( call.message ,get_name3 )


def get_name3(message):
    key = types.ReplyKeyboardMarkup ( True ,True )
    global name3
    name3 = message.text
    key.row ( "MeestExpress" ,"IH-Тайм" ,"Новая Почта" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* MDMA 1г = 900грн

    \U0001F3D9*Город:* """ + name3 + """

    \U0001F4E8*Почта:*""""""

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Выбери службу доставки*""" ,parse_mode = "Markdown" ,reply_markup = key )
    bot.register_next_step_handler ( message ,get_post3 )


def get_post3(message):
    global post3
    post3 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* MDMA 1г = 900грн

    \U0001F3D9*Город:* """ + name3 + """

    \U0001F4E8*Почта:* """ + post3 + """

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи данные для получения
    (Фамилию и инициалы)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_finish3 )


def get_finish3(message):
    global finish3
    finish3 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* MDMA 1г = 900грн

    \U0001F3D9*Город:* """ + name3 + """

    \U0001F4E8*Почта:* """ + post3 + """

    \U0001F464*ФИО:* """ + finish3 + """

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи свой номер телефона
    (Только цыфрами начиная с 0)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_age3 )


def get_age3(message):
    global age3
    while age3 == 0:
        try:
            age3 = int(message.text)
        except Exception:
            bot.send_message ( message.from_user.id ,"Цыфрами" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* MDMA 1г = 900грн

    \U0001F3D9*Город:* """ + name3 + """

    \U0001F4E8*Почта:* """ + post3 + """

    \U0001F464*ФИО:* """ + finish3 + """

    \U0001F4DE*Тел.* """ + str ( age3 ) + """

    \U0001F3E4*Отделение:*""""""

    *Введи почтовое отделение
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_number3 )


def get_number3(message):
    global number3
    while number3 == 0:
        try:
            number3 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"""\r *Цыфрами*""" ,parse_mode = "Markdown" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* MDMA 1г = 900грн

    \U0001F3D9*Город:* """ + name3 + """

    \U0001F4E8*Почта:* """ + post3 + """

    \U0001F464*ФИО:* """ + finish3 + """

    \U0001F4DE*Тел.* """ + str ( age3 ) + """

    \U0001F3E4*Отделение:* """ + str ( number3 ) + """

    *Введи количество которое тебе нужно
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_phone3 )


def get_phone3(message):
    keyboard1 = telebot.types.InlineKeyboardMarkup ( )
    global phone3
    while phone3 == 0:
        try:
            phone3 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Здесь используются только цифры" )
    kno1 = types.InlineKeyboardButton ( text = "Выбор товара" , callback_data = "1" )
    kno = types.InlineKeyboardButton ( text = "Связь с оператором\U0001F4DE" ,url = "https://t.me/DExpressBro" )
    keyboard1.add ( kno )
    keyboard1.add ( kno1 )
    bot.send_message ( message.from_user.id ,"""\r
                      *DrugExpress*
        `Товаро Транспортная Накладная` \U0001F4DD
       \U0001F194 """ + str ( random.randint ( 100000 ,200000 ) ) + """

    \U0001F6CD*Товар:* MDMA 1г = 900грн
    \U0001F3D9*Город:* """+ name3 +"""
    \U0001F4E8*Почта:* """+ post3 +"""
    \U0001F464*ФИО:* """+ finish3 +"""
    \U0001F4DE*Тел.* """+ str(age) + """
    \U0001F3E4*Отделение:* """ + str(number3) + """
    
    \U0001F4B0*Сумма:* """+str(phone3*900+50)+"""*грн*
     
    *Данные для отправки есть 
                Осталось оплатить заказ*
 `(`*Оплачивать нужно с рассчётом комиссии*`)`
                         
    \U0001F4B3`EasyPay` *- 66333880*
            
    *Сделай скрин оплаты \U0001F4F2
    \U0001F4E9 перешли это сообщение оператору* \U0001F464
    
    /start \U0001F449 Нажми и попадёшь в главное меню
    
    _Спасибо что выбрал наш сервис_ *DrugExpress*""", parse_mode="Markdown", reply_markup = keyboard1)



@bot.callback_query_handler ( func = lambda call: call.data == "5.1" )
def callback_next(call):
    if call.data == "5.1":
        bot.send_photo ( chat_id = call.message.chat.id, photo='https://imbt.ga/Jm6Fi3MgRI', caption = """\r
                      *DrugExpress*

        \U0001F6CD*Товар:* XTC 300мг = 300грн

        \U0001F3D9*Город:*

        \U0001F4E8*Почта:*

        \U0001F464*ФИО:*

        \U0001F4DE*Тел.*

        \U0001F3E4*Отделение:*

        *Напиши город 
        В который нужна доставка*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( call.message ,get_name4 )


def get_name4(message):
    key = types.ReplyKeyboardMarkup ( True ,True )
    global name4
    name4 = message.text
    key.row ( "MeestExpress" ,"IH-Тайм" ,"Новая Почта" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* XTC 300мг = 300грн

    \U0001F3D9*Город:* """ + name4 + """

    \U0001F4E8*Почта:*""""""

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Выбери службу доставки*""" ,parse_mode = "Markdown" ,reply_markup = key )
    bot.register_next_step_handler ( message ,get_post4 )


def get_post4(message):
    global post4
    post4 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* XTC 300мг = 300грн

    \U0001F3D9*Город:* """ + name4 + """

    \U0001F4E8*Почта:* """ + post4 + """

    \U0001F464*ФИО:*""""""

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи данные для получения
    (Фамилию и инициалы)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_finish4 )


def get_finish4(message):
    global finish4
    finish4 = message.text
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* XTC 300мг = 300грн

    \U0001F3D9*Город:* """ + name4 + """

    \U0001F4E8*Почта:* """ + post4 + """

    \U0001F464*ФИО:* """ + finish4 + """

    \U0001F4DE*Тел.*""""""

    \U0001F3E4*Отделение:*""""""

    *Введи свой номер телефона
    (Только цыфрами начиная с 0)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_age4 )


def get_age4(message):
    global age4
    while age4 == 0:
        try:
            age4 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Цыфрами" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* XTC 300мг = 300грн

    \U0001F3D9*Город:* """ + name4 + """

    \U0001F4E8*Почта:* """ + post4 + """

    \U0001F464*ФИО:* """ + finish4 + """

    \U0001F4DE*Тел.* """ + str ( age4 ) + """

    \U0001F3E4*Отделение:*""""""

    *Введи почтовое отделение
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_number4 )


def get_number4(message):
    global number4
    while number4 == 0:
        try:
            number4 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"""\r *Цыфрами*""" ,parse_mode = "Markdown" )
    bot.send_message ( message.from_user.id ,"""\r
                  *DrugExpress*

    \U0001F6CD*Товар:* XTC 300мг = 300грн

    \U0001F3D9*Город:* """ + name4 + """

    \U0001F4E8*Почта:* """ + post4 + """

    \U0001F464*ФИО:* """ + finish4 + """

    \U0001F4DE*Тел.* """ + str ( age4 ) + """

    \U0001F3E4*Отделение:* """ + str ( number4 ) + """

    *Введи количество которое тебе нужно
    (Только цыфрами)*""" ,parse_mode = "Markdown" )
    bot.register_next_step_handler ( message ,get_phone4 )


def get_phone4(message):
    keyboard1 = telebot.types.InlineKeyboardMarkup ( )
    global phone4
    while phone4 == 0:
        try:
            phone4 = int ( message.text )
        except Exception:
            bot.send_message ( message.from_user.id ,"Здесь используются только цифры" )
    kno1 = types.InlineKeyboardButton ( text = "Выбор товара" , callback_data = "1" )
    kno = types.InlineKeyboardButton ( text = "Связь с оператором\U0001F4DE" ,url = "https://t.me/DExpressBro" )
    keyboard1.add ( kno )
    keyboard1.add ( kno1 )
    bot.send_message ( message.from_user.id ,"""\r
                      *DrugExpress*
        ``` Товаро Транспортная Накладная``` \U0001F4DD
       \U0001F194 """ + str ( random.randint ( 100000 ,200000 ) ) + """

    \U0001F6CD*Товар:* XTC 300мг = 300грн
    \U0001F3D9*Город:* """+ name4 +"""
    \U0001F4E8*Почта:* """+ post4 +"""
    \U0001F464*ФИО:* """+ finish4 +"""
    \U0001F4DE*Тел.* """+ str(age) + """
    \U0001F3E4*Отделение:* """ + str(number4) + """
    
    \U0001F4B0*Сумма:* """+str(phone4*300+50)+"""*грн*
     
    *Данные для отправки есть 
                Осталось оплатить заказ*
 `(`*Оплачивать нужно с рассчётом комиссии*`)`
                         
    \U0001F4B3`EasyPay` *- 66333880*
            
    *Сделай скрин оплаты \U0001F4F2
    \U0001F4E9 перешли это сообщение оператору* \U0001F464
    
    /start \U0001F449 Нажми и попадёшь в главное меню
    
    _Спасибо что выбрал наш сервис_ *DrugExpress*""", parse_mode="Markdown", reply_markup = keyboard1)


bot.polling(none_stop=True, interval=0)