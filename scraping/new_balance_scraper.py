from bs4 import BeautifulSoup
from utils import Scraper

NB_URL = 'https://www.newbalance.com/men/shoes/running/?start=0&sz=10000'

class NewBalanceScraper(Scraper):
    pass

scraper = NewBalanceScraper('new balance', NB_URL)
scraper.scrape()
