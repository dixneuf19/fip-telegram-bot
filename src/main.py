import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from src.fip import get_live, get_stations

load_dotenv()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

BOT_TELEGRAM_TOKEN = os.getenv("BOT_TELEGRAM_TOKEN")


def display_help(update, context):
    help_message = """
This bot helps you share your love of FIP !

Commands :
/whatsonFIP - Display the current song played on FIP, and search for it on Spotify. Doesn't work during shows such Jazzafip
/live <RADIO_FRANCE_STATION>
    """
    update.message.reply_text(help_message)


updater = Updater(BOT_TELEGRAM_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler("whatsonFIP", get_live))
updater.dispatcher.add_handler(CommandHandler("live", get_live))
updater.dispatcher.add_handler(CommandHandler("stations", get_stations))
updater.dispatcher.add_handler(CommandHandler("help", display_help))
unknown_handler = MessageHandler(Filters.command, display_help)
updater.dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
