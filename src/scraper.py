# src/scraper.py

import requests
from bs4 import BeautifulSoup
import logging
from config.settings import HEADERS

logging.basicConfig(filename='logs/scraper.log', level=logging.INFO)

def scrape_data(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        logging.info(f"Successfully scraped {url}")
        return soup
    except requests.exceptions.RequestException as e:
        logging.error(f"Error scraping {url}: {e}")
        return None
