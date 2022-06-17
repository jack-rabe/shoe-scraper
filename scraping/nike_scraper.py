from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time

NIKE_URL = 'https://www.nike.com/w/mens-running-shoes-37v7jznik1zy7ok'

def parse_page(html, shoes_array):
    cards = html.find_all(class_='product-card__body')

    for card in cards:
        shoe = { 'brand': 'nike' }
        # find name of shoe
        shoe_name = card.find(class_='product-card__link-overlay').get_text()
        shoe['name'] = shoe_name
        # find price of shoe (sale price is listed first)
        price = card.find_all(class_='product-price')
        if price:
            shoe['price'] = price[0].get_text() 
        else:
            continue
        # get image src url
        img_url = card.find('img')['src']
        shoe['img_url'] = img_url
        # get url to go to individual shoe page
        shoe_page_url = card.find('a')['href']
        shoe['page_url'] = shoe_page_url
        # add shoe to list
        print(shoe)
        shoes_array.append(shoe)

shoes = []
driver = webdriver.Chrome()
driver.get(NIKE_URL)
driver.fullscreen_window()
for i in range(3):
    time.sleep(5)
    driver.execute_script(f'window.scrollTo(0, document.body.clientHeight);')
time.sleep(5)
page = driver.page_source
driver.close()

parsed_page = BeautifulSoup(page, 'html.parser')
parse_page(parsed_page, shoes)

# write output to json file
with open('../data/nike_shoes.json', 'w') as f:
    output = {
            'brand': 'nike',
            'count': len(shoes),
            'shoes': shoes
            }
    json.dump(output, f, indent=4)
