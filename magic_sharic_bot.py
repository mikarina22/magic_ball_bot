import telebot

import random

bot = telebot.TeleBot('___') #Вместо ___ вставить токен телеграм-бота

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

@bot.message_handler(commands=["oracle"])
def start(m, res=False):
    bot.send_message(m.chat.id, random.choice(answers))


bot.polling(none_stop=True, interval=0)
