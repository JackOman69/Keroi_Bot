import telebot
import consts

bot = telebot.TeleBot(consts.token)

# bot.send_message(509237723, "Привет!")

@bot.message_handler(content_type = "text")
def handle_text(message):
		if message.text == "Привет!":
				bot.send_message(509237723, "Здравствуй!")


bot.polling(none_stop = True, interval = 0)


 #upd = bot.get_updates()
 #last_upd = upd[-1]
 #message_from_user = last_upd.message
 #print(message_from_user)

