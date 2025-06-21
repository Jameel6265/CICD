import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [quote.text.strip() for quote in soup.select("span.text")]
    return quotes

if __name__ == "__main__":
    for q in scrape_quotes():
        print(q)
