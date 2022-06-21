from selenium import webdriver
from bs4 import BeautifulSoup
from utils import get_page_html, write_output

BROOKS_URL = 'https://www.brooksrunning.com/en_us/all-mens-running-shoes/'

def parse_page(html, shoes_array):
    cards = html.find_all(class_='m-product-tile') 

    for idx, card in enumerate(cards):
        shoe = { 'brand': 'brooks' }
        # find name of shoe
        shoe_name = card.find('h2').get_text().strip()
        shoe['name'] = shoe_name
        # find price of shoe (sale price is listed first)
        price = card.find_all(class_='pricing__sale')
        if price:
            price_str = price[-1].get_text().replace('$', '') 
            try:
                price = int(price_str)
            except:
                price = float(price_str)
            shoe['price'] = price
        else:
            continue
        # get image src url
        img_urls = card.find_all('img')
        for url in img_urls:
            url_src = url['src']
            if 'http' in url_src and 'award' not in url_src:
                shoe['img_url'] = url_src
                break

        # get url to go to individual shoe page
        shoe_page_url = card.find('a')['href']
        shoe['page_url'] = f'https://brooksrunning.com{shoe_page_url}'
        # add shoe to list
        shoes_array.append(shoe)


shoes = []
driver = webdriver.Chrome()
page = get_page_html(BROOKS_URL, driver)
parse_page(page, shoes)
write_output('brooks', shoes)
