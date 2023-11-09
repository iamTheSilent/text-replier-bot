from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext

from telegram import Update

from telegram.chataction import ChatAction

token = "UR TOKEN"


def start_handler(update: Update, context: CallbackContext):
    import pdb; pdb.set_trace()
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text("سلام {} {} \n به ربات پیامرسان خوش آمدید.".format(first_name, last_name))

def help_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text("استفاده ازین ربات خیلی راحته \n کافیه کمی فکر کنی")


def contactus_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text('ارتباط با ما فقط توسط آیدی زیر است \n @Shololow')


def bcs_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text('این کامند صرفا برای یاد آوری اینه که نشون بده سازنده این ربات به سریال \n better call saul \n علاقه منده')


updater = Updater(token, use_context=True)

start_command = CommandHandler("start", start_handler)
help_command = CommandHandler('help', help_handler)
contactus_command = CommandHandler('contactUs', contactus_handler)
bcs_command = CommandHandler('bcs', bcs_handler)

updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(help_command)
updater.dispatcher.add_handler(contactus_command)
updater.dispatcher.add_handler(bcs_command)

updater.start_polling()

updater.idle()