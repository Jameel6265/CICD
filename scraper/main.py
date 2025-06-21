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
        f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        f.write("<meta charset='UTF-8'>\n<title>Scraped Quotes</title>\n</head>\n<body>\n")
        f.write("<h1>Scraped Quotes</h1>\n<ul>\n")
        for q in quotes:
            f.write(f"<li>{q}</li>\n")
        f.write("</ul>\n</body>\n</html>")

if __name__ == "__main__":
    print("Scraping quotes from http://quotes.toscrape.com ...\n")
    for q in scrape_quotes():
        print(q)
    print("\nWriting quotes to output.html ...")
    write_to_file()
