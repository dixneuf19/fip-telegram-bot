import os
import logging

from telegram.ext import Updater, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode
from dotenv import load_dotenv

from src.api import get_live_on_FIP, LiveFIPException
from src.spotify import get_song_from_spotify, generate_link_from_uri
from src.utils import dict_to_simple_song
from src.fmt import song_to_markdown

load_dotenv()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

BOT_TELEGRAM_TOKEN = os.getenv("BOT_TELEGRAM_TOKEN")



def get_live(update, context):
    try:

        # get the song from FIP
        song = get_live_on_FIP()
        # song = dict_to_simple_song({"title": "Mango meat", "artist": "Mandrill"})
        
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=song_to_markdown(song),
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
            )

        # search the song on spotify
        spotify_track = get_song_from_spotify(song)
        if spotify_track is None:
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Not found on spotify",
            parse_mode=ParseMode.MARKDOWN_V2,
            )
        else:
            spot_txt = f"""Found this on Spotify :\n\n{generate_link_from_uri(spotify_track.uri)}"""
            
            context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=spot_txt,
            )
        
    except LiveFIPException:
         context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_markdown("The FIP API cannot inform us about the live, is it _Club Jazzafip_ ?"),
            parse_mode=ParseMode.MARKDOWN_V2,
            )
    except Exception as e:
        logging.error(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hum something went wrong...",
            )

def display_help(update, context):
    help_message = """
This bot helps you share your love of FIP !

Commands :
/live, /whatsonFIP - Display the current song played on FIP, and search for it on Spotify. Doesn't work during shows such Jazzafip
    """
    update.message.reply_text(help_message)


updater = Updater(BOT_TELEGRAM_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler("live", get_live))
updater.dispatcher.add_handler(CommandHandler("whatsonFIP", get_live))
updater.dispatcher.add_handler(CommandHandler("help", display_help))

updater.start_polling()
updater.idle()
