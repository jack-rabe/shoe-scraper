from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time

NIKE_URL = 'https://www.nike.com/w/mens-running-shoes-37v7jznik1zy7ok'

def get_page_html(url, driver):
    driver.get(url)
    driver.fullscreen_window()

    height = driver.execute_script("return document.body.scrollHeight")
    position = 700
    while position < height:
        driver.execute_script(f'window.scrollTo(0, { position });')
        time.sleep(3)
        height = driver.execute_script("return document.body.scrollHeight")
        position += 700
    time.sleep(3)
    page = driver.page_source
    driver.quit()

    parsed_page = BeautifulSoup(page, 'html.parser')
    return parsed_page


def parse_page(html, shoes_array):
    cards = html.find_all(class_='product-card__body')

    for card in cards:
        shoe = { 'brand': 'nike' }
        # find name of shoe
        shoe_name = card.find(class_='product-card__link-overlay').get_text()
        shoe['name'] = shoe_name.replace('Nike', '').strip()
        # find price of shoe (sale price is listed first)
        price = card.find_all(class_='product-price')
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
        shoe['page_url'] = shoe_page_url
        # add shoe to list
        shoes_array.append(shoe)


shoes = []
driver = webdriver.Chrome()
page = get_page_html(NIKE_URL, driver)
parse_page(page, shoes)

# write output to json file
with open('../data/nike_shoes.json', 'w') as f:
    output = {
            'brand': 'nike',
            'count': len(shoes),
            'shoes': shoes
            }
    json.dump(output, f, indent=4)
