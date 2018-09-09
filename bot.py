import telebot
import consts

bot = telebot.TeleBot(consts.token)

@bot.message_handler(commands=['start'])  
def handle_start(message):

		user_markup = telebot.types.ReplyKeyboardMarkup(True) 
		user_markup.row('/start', '/stop')
		user_markup.row('Фото', 'Аудио', 'Документы')
		user_markup.row('Стикер', 'Видео', 'Голос', 'Локации')
		bot.send_message(message.from_user.id, "Добро пожаловать...", reply_markup=user_markup)

@bot.message_handler (commands=['stop'])
def handle_stop(message):
		hide_markup = telebot.types.ReplyKeyboardRemove()
		bot.send_message(message.from_user.id, "До встречи!", reply_markup = hide_markup)

bot.polling(none_stop=True, interval=0)


































# @bot.message_handler(content_types = ["text"])
# def handle_text(message):
# 		if message.text == "Привет!":
# 				bot.send_message(message.from_user.id, "Здравствуй!")
# 		elif message.text == "Пока":
# 				bot.send_message(message.from_user.id, "Ну пока :c")		
# 		else:
# 				bot.send_message(message.from_user.id, "Попробуй еще раз!")


#upd = bot.get_updates()
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)
