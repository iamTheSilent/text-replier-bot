from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext.filters import Filters

 

from telegram import ReplyKeyboardMarkup
from telegram import Update

from telegram.chataction import ChatAction

token = "UR TOKEN"
message= {
    "msg_start":"سلام {} {} \n به ربات پیامرسان خوش آمدید.",
    "msg_help":"استفاده ازین ربات خیلی راحته \n کافیه کمی فکر کنی",
    "msg_contactUs":'ارتباط با ما فقط توسط آیدی زیر است \n @Shololow',
    "msg_bcs": 'این کامند صرفا برای یاد آوری اینه که نشون بده سازنده این ربات به سریال \n better call saul \n علاقه منده',
    "msg_sum": 'مجموع اعداد داده شده برابر با : \n {}',
    "msg_main_menu":"منو اصلی:",
    "msg_mokaleme_menu": "یکی از موارد زیر را انتخاب کنید",
    "msg_numid": "جسجتو با آیدی",
    "msg_random":"جستجوی رندوم",
    "msg_nonesense": "یکیوانتخاب کن",
    "bot_nonesense": "ته انبار",
    "bot_photo": "میخوای یه عکس ببینی؟",
    "bot_music":"یه موزیکمون نشه؟",
    "bot_search":"جسجتو مکالمه",
    "bot_profile":"پروفایل",
    "bot_contact":"انتقاد و پیشنهاد",
    "bot_return":"بازگشت"


}

def send_music_handler(update: Update, context: CallbackContext):
    Chat_id = update.message.chat_id
    with open("UR AUDIO FILE LOCATION", "rb") as music:
        context.bot.send_chat_action(Chat_id, ChatAction.UPLOAD_AUDIO)
        context.bot.sendAudio(Chat_id, music, caption= "my fav music these days", timeout= 5000)

def send_photo_handler(update: Update, context: CallbackContext):
    Chat_id = update.message.chat_id
    with open("UR PHOTO FILE LOCATION", "rb") as img:
        context.bot.send_chat_action(Chat_id, ChatAction.UPLOAD_PHOTO)
        context.bot.sendPhoto(Chat_id, img , caption= "my fav photo these days", timeout= 3000)

    

def main_menu_handler(update: Update, context: CallbackContext):
    buttons = [
        [message["bot_search"],message["bot_profile"]], 
        [message["bot_contact"]],
        [message["bot_nonesense"]],
        [message["bot_return"]]
    ]
    update.message.reply_text(
        text=message["msg_main_menu"],
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

def search_handler(update: Update, context: CallbackContext):
    buttons = [
        [message["msg_numid"], message["msg_random"]],
        [message["bot_return"]]
    ]
    update.message.reply_text(
        text=message["msg_mokaleme_menu"],
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    )

def nonesense_handler(update: Update, context:CallbackContext):
    buttons = [
        [message["bot_music"],
         message["bot_photo"]]
    ]
    update.message.reply_text(
        text=message["msg_nonesense"],
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    )
        
    



def start_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=message["msg_start"].format(first_name, last_name))
    main_menu_handler(update, context)

def help_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=message["msg_help"])


def contactus_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=message["msg_contactUs"])


def bcs_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=message["msg_bcs"])


def sum_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    numbers = context.args
    result = sum(int(i) for i in numbers)
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=message["msg_sum"].format(result))

def return_handler(update: Update, context: CallbackContext):
    main_menu_handler(update, context)

def main():
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help_handler))
    updater.dispatcher.add_handler(CommandHandler('contactUs', contactus_handler))
    updater.dispatcher.add_handler(CommandHandler('bcs', bcs_handler))
    updater.dispatcher.add_handler(CommandHandler('sum', sum_handler))
    updater.dispatcher.add_handler(CommandHandler("menu", main_menu_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(message["bot_search"]), search_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(message["bot_return"]), return_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(message["bot_music"]), send_music_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(message["bot_photo"]), send_photo_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(message["bot_nonesense"]), nonesense_handler))




    updater.start_polling()

    updater.idle()

main()