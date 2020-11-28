from typing import List

from telegram.utils.helpers import escape_markdown

from fip_telegram_bot.models import Track, Station


def track_to_markdown(track: Track) -> str:
    md = "*Live on [FIP](https://www.fip.fr) :*\n\n"

    md += "*" + escape_markdown(track.title, version=2) + "*\n"
    md += "_" + escape_markdown(track.artist, version=2) + "_\n"
    if track.album is not None:
        md += escape_markdown(track.album, version=2)
    if track.album is not None and track.year is not None:
        md += f" \- "
    if track.year is not None:
        md += escape_markdown(str(track.year), version=2)

    return md


def stations_to_markdown(stations: List[Station]) -> str:
    md = "*Stations Radio France :*\n\n"

    for station in stations:
        md += f"{escape_markdown(station.name, version=2)}\n"

    return md
