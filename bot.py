import telebot
import consts

bot = telebot.TeleBot(consts.token)

@bot.message_handler(commands = ["start"])
def handle_start(message):
		user_markup = telebot.types.ReplyKeyboardMarkup()
		user_markup.row("/start", "/stop")
		user_markup.row("фото", "аудио","документы")
		user_markup.row("стикер", "голос", "видео", "локация")
		bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup = user.markup)

# @bot.message_handler(content_types = ["text"])
# def handle_text(message):
# 		if message.text == "Привет!":
# 				bot.send_message(message.from_user.id, "Здравствуй!")
# 		elif message.text == "Пока":
# 				bot.send_message(message.from_user.id, "Ну пока :c")		
# 		else:
# 				bot.send_message(message.from_user.id, "Попробуй еще раз!")

if __name__ = "__name__":
		bot.polling(none_stop=True)


 #upd = bot.get_updates()
 #last_upd = upd[-1]
 #message_from_user = last_upd.message
 #print(message_from_user)

