from bs4 import BeautifulSoup
from scraper import Scraper

NB_URL = 'https://www.newbalance.com/men/shoes/running/?start=0&sz=10000'

class NewBalanceScraper(Scraper):
    def get_page_url(self, card, shoe):
        shoe_page_url = card.find('a')['href']
        shoe['page_url'] = f'https://newbalance.com{shoe_page_url}'

scraper = NewBalanceScraper(
        brand_name = 'new balance',
        url = NB_URL,
        card_class = 'product-tile',
        name_class = 'pname',
        price_class = 'sales',
        price_idx = 0
        ).scrape()
