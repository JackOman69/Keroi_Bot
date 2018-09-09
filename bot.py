import telebot
import consts

bot = telebot.TeleBot(consts.token)

@bot.message_handler(content_types = ["help"])
		def handle_text(message):
				print("""Этот бот пока может отвечать на две команды.
								 Но это не предел!""")




@bot.message_handler(content_types = ["text"])
def handle_text(message):
		if message.text == "Привет!":
				bot.send_message(message.from_user.id, "Здравствуй!")
		elif message.text == "Пока":
				bot.send_message(message.from_user.id, "Ну пока :c")		
		else:
				bot.send_message(message.from_user.id, "Попробуй еще раз!")


bot.polling(none_stop=True)


 #upd = bot.get_updates()
 #last_upd = upd[-1]
 #message_from_user = last_upd.message
 #print(message_from_user)

