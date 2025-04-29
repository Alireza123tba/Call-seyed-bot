import requests
import logging

def fetch_data_mevx():
    url = 'https://api.mevx.io/v1/pairs'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.exception("Error fetching data from MEVX")
        return []

def fetch_data_dexscreener():
    url = 'https://api.dexscreener.com/latest/dex/tokens'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.exception("Error fetching data from Dexscreener")
        return []
