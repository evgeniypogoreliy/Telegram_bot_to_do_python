from email import message
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, filters, MessageHandler
from modules import *

bot = Bot('5524005949:AAEjN-NjqLTZ23pYe_lq6RXZOPdcbp4DbkU')
updater = Updater('5524005949:AAEjN-NjqLTZ23pYe_lq6RXZOPdcbp4DbkU')
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(filters.text, message)
unknown_handler = MessageHandler(filters.command, unknown)
to_do_handler = CommandHandler('to_do', to_do)

dispatcher.add_handler(to_do_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('Прогоама запущена!')
updater.start_polling()
updater.idle()
