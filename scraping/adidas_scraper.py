from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
import time

ADIDAS_URL = 'https://www.adidas.com/us/men-running-shoes'
SHOES_PER_PAGE = 48 


def get_page_html(url, driver):
    driver.get(url)
    # load page slowly to retrieve prices
    time.sleep(5)
    for i in range(1, 10):
        time.sleep(3)
        driver.execute_script(f'window.scrollTo(0, {i * 700});')
    page = driver.page_source
    parsed_page = BeautifulSoup(page, 'html.parser')
    parse_shoe_count(parsed_page)
    return parsed_page


def parse_shoe_count(html):
    shoe_count = html.find(class_='count___1ZIhY').get_text()
    shoe_count = shoe_count.replace('[', '')
    shoe_count = shoe_count.replace(']', '')
    return int(shoe_count)


def parse_page(html, shoes_array):
    cards = html.find_all(class_='glass-product-card-container', recursive=True)

    for card in cards:
        shoe = { 'brand': 'adidas' }
        # find name of shoe
        shoe_name = card.find(class_='glass-product-card__title')
        if shoe_name:
            shoe['name'] = shoe_name.get_text()
        else:
            shoe['name'] = card.find(class_='glass-product-card__details').get_text()
        # find price of shoe (the sale price is always listed last)
        price = card.find_all(class_='gl-price-item')
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
        img_url = card.find('img')['src']
        shoe['img_url'] = img_url
        # get url to go to individual shoe page
        shoe_page_url = card.find('a')['href']
        # some urls need to be prefixed with adidas.com
        if re.search('^/us/', shoe_page_url):
            shoe_page_url = f'https://www.adidas.com{shoe_page_url}' 
        shoe['page_url'] = shoe_page_url
        # add shoe to list
        shoes_array.append(shoe)


driver = webdriver.Chrome()
url = ADIDAS_URL
page_offset = 48
shoes = []
while True:
    page = get_page_html(url, driver)
    parse_page(page, shoes)
    shoe_count = parse_shoe_count(page)
    url = ADIDAS_URL + f'?start={page_offset}'
    # exit once all pages have been read
    if page_offset > shoe_count:
        break
    page_offset += 48

driver.quit()

# write output to json file
with open('../data/adidas_shoes.json', 'w') as f:
    output = { 
            'brand' : 'adidas',
            'count': len(shoes),
            'shoes': shoes 
            } 
    json.dump(output, f, indent=4)
