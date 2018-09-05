import telebot
import consts

bot = telebot.TeleBot(contst.token)

bot.send_message(509237723, "Привет!")

upd = bot.get_updates()
print(upd)

