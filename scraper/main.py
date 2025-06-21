import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [quote.text.strip() for quote in soup.select("span.text")]
    return quotes

def write_to_file():
    quotes = scrape_quotes()
    with open("output.html", "w", encoding="utf-8") as f:
        f.write("<h1>Scraped Quotes</h1>\n<ul>")
        for q in quotes:
            f.write(f"<li>{q}</li>")
        f.write("</ul>")

if __name__ == "__main__":
    for q in scrape_quotes():
        print(q)
    write_to_file()    
