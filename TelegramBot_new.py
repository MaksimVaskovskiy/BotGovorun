import random
import telebot

from telebot import types
from random import choice

bot = telebot.TeleBot('***')


rand_dialog = ['Привет', 'Как твои дела?', 'Вы что то имеете мне сказать?',
'Перестань истерить!', 'И не ори мне', 'Я тебя прекрасно слышу',
'Не ори на меня я тебе говорю!', 'Я тебе во внуки гожусь!', 'Кто я?', 'Где я?', 'Кто сдесь?',
'Я тебя знаю?', 'Мы что, с тобой знакомы?', 'Я умею материться', 'Хошь сматерюсь?', 'Сейчас точно матом ругаться начну!']

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветствую тебя, <b><u>{message.from_user. first_name} {message.from_user. last_name}</u></b>! ' \
           f'Чем могу быть полезен?'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    donate = types.KeyboardButton('Donate')
    thanks = types.KeyboardButton('Thanks')
    markup.add(donate, thanks)
    bot.send_message(message.chat.id, 'Поблагодарите автора, не будь жадиной!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    fraza = message.text
    task = random.choice(rand_dialog)
    rand_dialog.append(fraza)
    bot.send_message(message.chat.id, task, parse_mode='html')
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе Шалом!", parse_mode='html')
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе Шалом!", parse_mode='html')
    elif message.text == 'ID':
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == 'photo':  # на сообщение 'photo' пользователь получет картинку в ответ
        photo = open('Bob.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "словарный запас":
        print(rand_dialog)



# команда принимает фото от пользователя и отвечает ему текстовым сообщением
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
     bot.send_message(message.chat.id, 'Вау крутое фото, ну ты крассава!')







bot.polling(none_stop=True)
