import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from fip_telegram_bot.fip import (
    get_feelgood,
    get_live,
    get_meuh,
    get_fiftyfity,
)

load_dotenv()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

BOT_TELEGRAM_TOKEN = os.getenv("BOT_TELEGRAM_TOKEN")
BOT_WEBHOOK_PATH = os.getenv("BOT_WEBHOOK_PATH")

USE_POLLING = os.getenv("USE_POLLING") in ("True", "true", "1")


def display_help(update, context):
    help_message = """
This bot helps you share your love of FIP and other radios! 

It tries to fetch the live of the radio you are listening to and share it with your friends. It also adds a link to the song on Spotify.

The following radios are supported:
FIP - /live /whatsonFIP
RadioMeuh - /meuh
Radio5050 - /5050
FeelGood - /feelgood /fg
    """
    update.message.reply_text(help_message)


updater = Updater(BOT_TELEGRAM_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler("whatsonFIP", get_live))
updater.dispatcher.add_handler(CommandHandler("live", get_live))
updater.dispatcher.add_handler(CommandHandler("meuh", get_meuh))
updater.dispatcher.add_handler(CommandHandler("5050", get_fiftyfity))
updater.dispatcher.add_handler(CommandHandler("feelgood", get_feelgood))
updater.dispatcher.add_handler(CommandHandler("fg", get_feelgood))
updater.dispatcher.add_handler(CommandHandler("help", display_help))
unknown_handler = MessageHandler(Filters.command, display_help)
updater.dispatcher.add_handler(unknown_handler)

if USE_POLLING:
    updater.start_polling()
    logging.info("Start polling")
    updater.idle()

else:
    # add handlers
    updater.start_webhook(listen="0.0.0.0", port=80, url_path=BOT_WEBHOOK_PATH)
    updater.bot.set_webhook(f"https://fip-telegram-bot.dixneuf19.me/{BOT_WEBHOOK_PATH}")
    updater.idle()
