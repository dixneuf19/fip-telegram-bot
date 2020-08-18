import os
import logging
import requests
from requests import codes
from dotenv import load_dotenv
from typing import Union, List

from src.models import SimpleSong, Track, Station
from src.utils import dict_to_track, dict_to_simple_song, dict_to_station

load_dotenv()

FIP_API_HOST = os.getenv("FIP_API_HOST", "whats-on-fip")
FIP_API_PORT = os.getenv("FIP_API_PORT", "80")

SPOTIFY_API_HOST = os.getenv("SPOTIFY_API_HOST", "spotify-api") 
SPOTIFY_API_PORT = os.getenv("SPOTIFY_API_PORT", "80") 

class LiveFIPException(Exception):
    pass


def get_live_on_FIP() -> SimpleSong:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/live"
    logging.info(f"Fetching live info from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return dict_to_simple_song(r.json())
    elif r.status_code == codes.no_content:
        logging.warning(f"FIP API is up but is unable to fetch the live")
        raise LiveFIPException()
        
    r.raise_for_status()

def get_live_on_station(station_name: str) -> SimpleSong:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/live?station={station_name}"
    logging.info(f"Fetching live info from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return dict_to_simple_song(r.json())
    elif r.status_code == codes.no_content:
        logging.warning(f"Radio France API is up but is unable to fetch the live")
        raise LiveFIPException()
        
    r.raise_for_status()

def get_radio_france_stations() -> List[Station]:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/stations"
    logging.info(f"Fetching Radio France stations from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return [dict_to_station(e) for e in r.json()]
    else:        
        r.raise_for_status()

def search_on_spotify(query: str) -> Union[SimpleSong, None]:
    logging.info(f"search for '{query}' on Spotify API")
    service_address = f"http://{SPOTIFY_API_HOST}:{SPOTIFY_API_PORT}/search"
    payload = {"q": query}
    r = requests.get(service_address, params=payload)
    if r.status_code == codes.not_found:
        logging.warning(f"no song found on Spotify with query '{query}'")
        return None
    r.raise_for_status()
    return dict_to_track(r.json())

def get_radio_france_api_status() -> str:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/api-status"
    logging.info(f"Fetching Radio France OpenAPI status")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return "Radio France OpenAPI is up"
    else:
        return f"Radio France OpenAPI is down with error code '{r.status_code}'"