import logging
from typing import Dict, Any

from src.models import SimpleSong, Artist, Image, Album, Track, Station

def dict_to_simple_song(obj: Dict[str, Any]) -> SimpleSong:
    try:
        return SimpleSong(
            title = obj["title"], # mandatory
            album = obj["album"] if "album" in obj else None,
            artist = obj["artist"], # mandatory
            year = obj["year"] if "year" in obj else None,
        )
    except:
        logging.error(f"failed to parse as simple song : {obj}")
        return None

def dict_to_track(obj: Dict[str,Any]) -> Track:
    try:
        return Track(
            album=dict_to_album(obj["album"]),
            artists=[dict_to_artist(art) for art in obj["artists"]],
            duration_ms=obj["duration_ms"],
            id=obj["id"],
            preview_url=obj["preview_url"],
            uri=obj["uri"],
            name=obj["name"],
        )
    except KeyError:
        return None


def dict_to_image(obj: Dict[str,Any]) -> Image:
    try:
        return Image(height=obj["height"], url=obj["url"], width=obj["width"],)
    except KeyError:
        return None


def dict_to_album(obj: Dict[str,Any]) -> Album:
    try:
        return Album(
            id=obj["id"],
            images=[dict_to_image(img) for img in obj["images"]],
            href=obj["href"],
            name=obj["name"],
            release_date=obj["release_date"],
            uri=obj["uri"],
        )
    except KeyError:
        return None


def dict_to_artist(obj: Dict[str,Any]) -> Artist:
    try:
        return Artist(
            id=obj["id"], href=obj["href"], name=obj["name"], uri=obj["uri"],
        )
    except KeyError:
        return None


def dict_to_station(obj: Dict[str, Any]) -> Station:
    try:
        return Station(
            name=obj["name"]
        )
    except KeyError:
        return None
