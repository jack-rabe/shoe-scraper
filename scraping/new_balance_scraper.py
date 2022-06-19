from selenium import webdriver
from bs4 import BeautifulSoup
from utils import get_page_html, write_output

NB_URL = 'https://www.newbalance.com/men/shoes/running/?start=0&sz=10000'

def parse_page(html, shoes_array):
    cards = html.find_all(class_='product-tile')

    for card in cards:
        shoe = { 'brand': 'new balance' }
        # find name of shoe
        shoe_name = card.find(class_='pname').get_text()
        shoe['name'] = shoe_name
        # find price of shoe (sale price is listed first)
        price = card.find_all(class_='sales')
        if price:
            price_str = price[0].get_text().replace('$', '') 
            try:
                price = int(price_str)
            except:
                price = float(price_str)
            shoe['price'] = price
        else:
            continue
        # get image src url
        img_url = card.find('img')['src']
        shoe['img_url'] = img_url
        # get url to go to individual shoe page
        shoe_page_url = card.find('a')['href']
        shoe['page_url'] = f'https://newbalance.com{shoe_page_url}'
        # add shoe to list
        shoes_array.append(shoe)


shoes = []
driver = webdriver.Chrome()
page = get_page_html(NB_URL, driver)
parse_page(page, shoes)
write_output('new balance', shoes)
