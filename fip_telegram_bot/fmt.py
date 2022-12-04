from typing import List

from telegram.utils.helpers import escape_markdown

from fip_telegram_bot.models import Track, Radio

FIP_RADIO = Radio(name="FIP", url="https://www.fip.fr")
MEUH_RADIO = Radio(name="Radiomeuh", url="https://www.radiomeuh.com/")
FIFTYFIFTY_RADIO = Radio(name="Radio5050", url="https://www.radio5050.com/")
FEELGOOD_RADIO = Radio(name="Radio FG \- Feel Good", url="https://www.radiofg.com/")


def track_to_markdown(track: Track, radio=FIP_RADIO) -> str:
    md = f"*Live on [{radio.name}]({radio.url}) :*\n\n"

    md += "*" + escape_markdown(track.title, version=2) + "*\n"
    md += "_" + escape_markdown(track.artist, version=2) + "_\n"
    if track.album is not None:
        md += escape_markdown(track.album, version=2)
    if track.album is not None and track.year is not None:
        md += f" \- "
    if track.year is not None:
        md += escape_markdown(str(track.year), version=2)

    return md
