import os
import logging

from telegram.ext import Updater, CommandHandler
from telegram import Audio
from dotenv import load_dotenv

from src.api import get_live_on_FIP, LiveFIPException
from src.spotify import get_song_from_spotify, generate_link_from_uri
from src.utils import dict_to_simple_song
from src.fmt import song_to_markdown

load_dotenv()

BOT_TELEGRAM_TOKEN = os.getenv("BOT_TELEGRAM_TOKEN")



def get_live(update, context):
    try:

        # get the song from FIP
        # song = get_live_on_FIP()
        song = dict_to_simple_song({"title": "Mango meat", "artist": "Mandrill"})
        update.message.reply_markdown_v2(song_to_markdown(song), disable_web_page_preview=True)

        # search the song on spotify
        spotify_track = get_song_from_spotify(song)
        if spotify_track is None:
            update.message.reply_markdown_v2("Not found on spotify")
        else:
            update.message.reply_text(
                f"""
                Found this on Spotify :\n\n{generate_link_from_uri(spotify_track.uri)}
                """
            )
        
        
        logging.warning(spotify_track)
    except LiveFIPException:
        update.message.reply_markdown_v2("The FIP API cannot inform us about the live, is it _Club Jazzafip_ ?")
    except Exception as e:
        logging.error(e)
        update.message.reply_text("Hum something went wrong...")

def display_help(update, context):
    help_message = """
This bot helps you share your love of FIP !

Commands :
/live - Display the current song played on FIP, and search for it on Spotify. Doesn't work during shows such Jazzafip
    """
    update.message.reply_text(help_message)


updater = Updater(BOT_TELEGRAM_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler("live", get_live))
updater.dispatcher.add_handler(CommandHandler("help", display_help))

updater.start_polling()
updater.idle()