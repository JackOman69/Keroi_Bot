import telebot

bot = telebot.Telebot(token = "682595564:AAH-nTcnj255cHSbuEXLq09SjzOrwwx4W7Y")

@bot.message_handler(content_types=("text"))

def send_message(message):
		bot.reply_to(message.chat.id, message.text)

if __name__ == "__main__":
		bot.polling(none_stop = True)


