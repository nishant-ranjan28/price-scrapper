from src.scraper import scrape_data
from src.parser import parse_data
from config.settings import URL

def main():
    raw_html = scrape_data(URL)
    processed_data = parse_data(raw_html)
    # Save or process the data as needed

if __name__ == "__main__":
    main()
