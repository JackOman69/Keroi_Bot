import telebot
import consts

bot = telebot.TeleBot(consts.token)

bot.send_message(509237723, "Привет!")

upd = bot.get_updates()

last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

