from typing import List

from telegram.utils.helpers import escape_markdown

from fip_telegram_bot.models import SimpleSong, Station


def song_to_markdown(song: SimpleSong) -> str:
    md = "*Live on [FIP](https://www.fip.fr) :*\n\n"

    md += "*" + escape_markdown(song.title, version=2) + "*\n"
    md += "_" + escape_markdown(song.artist, version=2) + "_\n"
    if song.album is not None:
        md += escape_markdown(song.album, version=2)
    if song.album is not None and song.year is not None:
        md += f" \- "
    if song.year is not None:
        md += escape_markdown(str(song.year), version=2)

    return md


def stations_to_markdown(stations: List[Station]) -> str:
    md = "*Stations Radio France :*\n\n"

    for station in stations:
        md += f"{escape_markdown(station.name, version=2)}\n"

    return md
