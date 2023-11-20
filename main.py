import sqlite3
import telebot
import info as info  # ваш файл

bot = telebot.TeleBot(token=info.API_TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(telebot.types.InlineKeyboardButton(info.button_1, callback_data='button_1'))

    photo = open('./img/photo_1.jpg', 'rb')

    bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=info.text_1, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'button_1':
        bot.send_message(chat_id=call.message.chat.id, text=info.text_2)

if __name__ == '__main__':
    bot.polling()