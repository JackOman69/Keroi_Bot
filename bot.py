import telebot
import consts

bot = telebot.TeleBot(consts.token)

bot.send_message(509237723, "Привет!")




