import logging

from telegram import ParseMode
from telegram.utils.helpers import escape_markdown

from fip_telegram_bot.api import (
    LiveFIPException,
    get_radio_france_stations,
    get_live_on_station,
    get_radio_france_api_status,
    get_live_on_meuh,
    get_live_on_fiftyfifty,
    get_live_on_feelgood,
)
from fip_telegram_bot.fmt import (
    track_to_markdown,
    stations_to_markdown,
    MEUH_RADIO,
    FIFTYFIFTY_RADIO,
    FEELGOOD_RADIO,
)


def get_live(update, context):
    update_message = update.message
    logging.info(
        f"Got '{update_message.text}' from {update_message.from_user.username} in {update_message.chat.title}"
    )
    try:
        # 1. get the track from FIP
        args = context.args
        if len(args) == 0:
            track = get_live_on_station("FIP")
        else:
            station_name = args[0]
            track = get_live_on_station(station_name)

        logging.info(f"Found this song live: {str(track)}")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=track_to_markdown(track),
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
        )

        # 2. send a link with the music

        for track_provider in ["spotify", "youtube", "deezer", "itunes"]:
            if track_provider in track.external_urls.keys():
                msg = f"""Found this on {track_provider.title()} !\n\n{track.external_urls[track_provider]}"""
                logging.info(msg.replace("\n", " "))
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=msg,
                )
                return

        logging.info("No external urls found")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Not found on Spotify 😢",
            parse_mode=ParseMode.MARKDOWN_V2,
        )

    except LiveFIPException:
        logging.info("No track information available right now")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_markdown(
                "No live song information right now, is it ", version=2
            )
            + "_Club Jazzafip_"
            + escape_markdown(" ?", version=2),
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    except Exception as e:
        logging.error(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_markdown(
                "Hum something went wrong... 😢 \nIs the API up ? Try /status and/or ping @dixneuf19 !",
                version=2,
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )


def get_meuh(update, context):
    update_message = update.message
    logging.info(
        f"Got '{update_message.text}' from {update_message.from_user.username} in {update_message.chat.title}"
    )
    try:
        # 1. get the track from Radiomeuh
        track = get_live_on_meuh()

        logging.info(f"Found this song live: {str(track)}")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=track_to_markdown(track, radio=MEUH_RADIO),
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
        )

        # 2. send a link with the music

        for track_provider in ["spotify", "youtube", "deezer", "itunes"]:
            if track_provider in track.external_urls.keys():
                msg = f"""Found this on {track_provider.title()} !\n\n{track.external_urls[track_provider]}"""
                logging.info(msg.replace("\n", " "))
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=msg,
                )
                return

        logging.info("No external urls found")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Not found on Spotify 😢",
            parse_mode=ParseMode.MARKDOWN_V2,
        )

    except Exception as e:
        logging.error(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_markdown(
                "Hum something went wrong... 😢 \nIs the API up ? Try /status and/or ping @dixneuf19 !",
                version=2,
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )


def get_fiftyfity(update, context):
    update_message = update.message
    logging.info(
        f"Got '{update_message.text}' from {update_message.from_user.username} in {update_message.chat.title}"
    )
    try:
        # 1. get the track from Radiofiftyfity
        track = get_live_on_fiftyfifty()

        logging.info(f"Found this song live: {str(track)}")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=track_to_markdown(track, radio=FIFTYFIFTY_RADIO),
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
        )

        # 2. send a link with the music

        for track_provider in ["spotify", "youtube", "deezer", "itunes"]:
            if track_provider in track.external_urls.keys():
                msg = f"""Found this on {track_provider.title()} !\n\n{track.external_urls[track_provider]}"""
                logging.info(msg.replace("\n", " "))
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=msg,
                )
                return

        logging.info("No external urls found")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Not found on Spotify 😢",
            parse_mode=ParseMode.MARKDOWN_V2,
        )

    except Exception as e:
        logging.error(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_markdown(
                "Hum something went wrong... 😢 \nIs the API up ? Try /status and/or ping @dixneuf19 !",
                version=2,
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )


def get_feelgood(update, context):
    update_message = update.message
    logging.info(
        f"Got '{update_message.text}' from {update_message.from_user.username} in {update_message.chat.title}"
    )
    try:
        # 1. get the track from Radiofeelgood
        track = get_live_on_feelgood()

        logging.info(f"Found this song live: {str(track)}")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=track_to_markdown(track, radio=FEELGOOD_RADIO),
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
        )

        # 2. send a link with the music

        for track_provider in ["spotify", "youtube", "deezer", "itunes"]:
            if track_provider in track.external_urls.keys():
                msg = f"""Found this on {track_provider.title()} !\n\n{track.external_urls[track_provider]}"""
                logging.info(msg.replace("\n", " "))
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=msg,
                )
                return

        logging.info("No external urls found")
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Not found on Spotify 😢",
            parse_mode=ParseMode.MARKDOWN_V2,
        )

    except Exception as e:
        logging.error(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=escape_markdown(
                "Hum something went wrong... 😢 \nIs the API up ? Try /status and/or ping @dixneuf19 !",
                version=2,
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )


def get_stations(update, context):
    update_message = update.message
    logging.info(
        f"Got '{update_message.text}' from {update_message.from_user.username} in {update_message.chat.title}"
    )
    stations = get_radio_france_stations()

    md = stations_to_markdown(stations)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=md,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def get_api_status(update, context):
    update_message = update.message
    logging.info(
        f"Got '{update_message.text}' from {update_message.from_user.username} in {update_message.chat.title}"
    )
    status_text = get_radio_france_api_status()

    logging.info(status_text)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=escape_markdown(status_text, version=2),
        parse_mode=ParseMode.MARKDOWN_V2,
    )
