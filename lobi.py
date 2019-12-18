import telebot
from telebot import types
import random


import starter

bot = telebot.TeleBot(starter.token)
#bot.send_message(466835416, "test")
upd = bot.get_updates()
#print(upd)
print(bot.get_me())


a = 42
b = "qwerty"

print(type(a), type(b))

@bot.message_handler(commands=['start']) #Запуск бота
def start_command(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    kno1 = types.InlineKeyboardButton(text="\U0001F4B0Первый способ\U0001F4B0", url="https://www.dinero.ua/aff/WYE28891")
    kno3 = types.InlineKeyboardButton(text="\U0001F4B0Второй способ\U0001F4B0", url="https://moneyveo.ua/?referral=a162ae65-860d-4353-8950-887773e969e8&utm_source=friends&utm_medium=cpa&utm_campaign=friends")
    keyboardmain.add(kno1)
    keyboardmain.add(kno3)

    bot.send_message(message.chat.id, """\r 
    *Раз ты зашёл до меня
    То тебе срочно понадобились деньги
    У меня есть дело
    За которое ты получишь 300 UAH*                   
    
    \U0001F4CD*Выбераете любой способ*\U0001F447
    `(`_каждый способ одноразовый_`)`
    
    \U0001F4CD*Там вы оформляете первый займ*\U0001F4DD
    `(`_300 гривен минимальный займ_`)`
    
    \U0001F4CD*После успешного офрмления*\U0001F44D
    `(`_Вам на карту прийдёт 300 гривен займа_`)`
    
    \U0001F4CD*После получения денег*\U0001F4B3
    `(`_вам нужно будет на сайте способа вернуть займ этими же деньгами_`)`
    
    \U0001F4CD*После успешного погашения займа*\U0001F911
    `(`_вам будет на счёт зачислины 300 гривен_`)`

    `Не влаживай
    А зарабатывай`
    """, parse_mode="Markdown", reply_markup=keyboardmain)





bot.polling(none_stop=True, interval=0)