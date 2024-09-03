# src/main.py

import pandas as pd
from src.scraper import scrape_data
from src.parser import parse_data
from config.settings import URL

def main():
    raw_html = scrape_data(URL)
    if raw_html:
        processed_data = parse_data(raw_html)
        # Convert to a DataFrame and save to CSV (optional)
        df = pd.DataFrame(processed_data)
        df.to_csv('data/processed/data.csv', index=False)
        print("Data saved to data/processed/data.csv")

if __name__ == "__main__":
    main()
