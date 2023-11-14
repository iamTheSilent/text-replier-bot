from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext

from telegram import Update

from telegram.chataction import ChatAction

token = "5914279686:AAHKD0-Autn8ZNbynpgjG3pZHQZpoBxiRus"
message= {
    "msg_start":"سلام {} {} \n به ربات پیامرسان خوش آمدید.",
    "msg_help":"استفاده ازین ربات خیلی راحته \n کافیه کمی فکر کنی",
    "msg_contactUs":'ارتباط با ما فقط توسط آیدی زیر است \n @Shololow',
    "msg_bcs": 'این کامند صرفا برای یاد آوری اینه که نشون بده سازنده این ربات به سریال \n better call saul \n علاقه منده',
    "msg_sum": 'مجموع اعداد داده شده برابر با : \n {}'



}


def start_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text="msg_start".format(first_name, last_name))

def help_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text="msg_help")


def contactus_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text="msg_contactUs")


def bcs_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text="msg_bcs")


def sum_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    numbers = context.args
    result = sum(int(i) for i in numbers)
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text="msg_sum".format(result))

def main():
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help_handler))
    updater.dispatcher.add_handler(CommandHandler('contactUs', contactus_handler))
    updater.dispatcher.add_handler(CommandHandler('bcs', bcs_handler))
    updater.dispatcher.add_handler(CommandHandler('sum', sum_handler))

    updater.start_polling()

    updater.idle()

main()