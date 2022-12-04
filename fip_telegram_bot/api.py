import os
import logging
import requests
from requests import codes
from dotenv import load_dotenv

from fip_telegram_bot.models import Track

load_dotenv()

FIP_API_HOST = os.getenv("FIP_API_HOST", "whats-on-fip")
FIP_API_PORT = os.getenv("FIP_API_PORT", "80")


class LiveFIPException(Exception):
    pass


def get_live_on_FIP() -> Track:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/live"
    logging.info(f"Fetching live info from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return Track(**r.json())
    elif r.status_code == codes.no_content:
        logging.warning(f"Radio France API is up but is unable to fetch the live")
        raise LiveFIPException()

    r.raise_for_status()


def get_live_on_meuh() -> Track:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/meuh"
    logging.info(f"Fetching live info from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return Track(**r.json())

    r.raise_for_status()


def get_live_on_fiftyfifty() -> Track:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/5050"
    logging.info(f"Fetching live info from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return Track(**r.json())

    r.raise_for_status()


def get_live_on_feelgood() -> Track:
    service_address = f"http://{FIP_API_HOST}:{FIP_API_PORT}/feelgood"
    logging.info(f"Fetching live info from {service_address}")
    r = requests.get(service_address)
    if r.status_code == codes.ok:
        return Track(**r.json())

    r.raise_for_status()
