import logging

from telegram import ParseMode
from telegram.utils.helpers import escape_markdown

from src.api import get_live_on_FIP, LiveFIPException, get_radio_france_stations, get_live_on_station
from src.spotify import get_song_from_spotify, generate_link_from_uri
from src.utils import dict_to_simple_song
from src.fmt import song_to_markdown, stations_to_markdown

def get_live(update, context):
    try:
        # get the song from FIP
        args = context.args
        if len(args) == 0:
            song = get_live_on_station("FIP")
        else:
            station_name = args[0]
            song = get_live_on_station(station_name)
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

def get_stations(update, context):
    stations = get_radio_france_stations()

    md = stations_to_markdown(stations)

    logging.info(md)

    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=md,
            parse_mode=ParseMode.MARKDOWN_V2,
            )
