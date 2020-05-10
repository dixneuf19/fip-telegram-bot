from typing import List, Union

from src.api import search_on_spotify
from src.models import SimpleSong, Track


def generate_queries(song: SimpleSong) -> List[str]:
    short_title = ' '.join(song.title.split()[:2]) if song.title is not None else ''
    short_artist = ' '.join(song.artist.split()[:2]) if song.artist is not None else ''
    queries = {
        "full_query": f"{song.title} {song.artist}",
        "short_query": f"{short_title} {short_artist}",
        "title": song.title,
    }

    return list(queries.values())

def get_song_from_spotify(song: SimpleSong) -> Union[Track, None]:
    track = None
    queries = generate_queries(song)
    for q in queries:
        track = search_on_spotify(q)
        if track is not None:
            break
    return track

def generate_link_from_uri(uri: str) -> str:
    ressource_type, ressource_id = uri.split(":")[-2:]
    return f"https://open.spotify.com/{ressource_type}/{ressource_id}"