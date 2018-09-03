import telebot

bot = telebot.TeleBot(token="682595564:AAH-nTcnj255cHSbuEXLq09SjzOrwwx4W7Y")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
		bot.reply_to(message, 'How are you, nigga?')




