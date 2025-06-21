from scraper.main import scrape_quotes

def test_scrape_quotes():
    quotes = scrape_quotes()
    assert isinstance(quotes, list)
    assert len(quotes) > 0
    assert quotes!=''
