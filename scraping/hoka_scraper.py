from bs4 import BeautifulSoup
from selenium import webdriver
from utils import get_page_html, write_output

HOKA_URL = 'https://www.hoka.com/en/us/mens-view-all/?sz=10000'

def parse_page(html, shoes_array):
    cards = html.find_all(class_='product')

    for card in cards:
        shoe = { 'brand': 'hoka' }
        # find name of shoe
        name_div = card.find(class_='tile-product-name')
        shoe_name = name_div.find('a').get_text()
        shoe['name'] = shoe_name.replace("Men's", '').replace('All Gender', '').strip()
        # find price of shoe (sale price is listed first)
        price = card.find(class_='sales')
        if price:
            price_str = price.get_text().replace('$', '') 
            try:
                price = int(price_str)
            except:
                price = float(price_str)
            shoe['price'] = price
        # get image src url
        img_url = card.find('img')['src']
        shoe['img_url'] = img_url
        # get url to go to individual shoe page
        shoe_page_url = f"https://hoka.com{name_div.find('a')['href']}"
        shoe['page_url'] = shoe_page_url
        # add shoe to list (if it is a running shoe)
        is_running_shoe = False
        for purpose in card.find_all(class_='best-for__surface'):
            if 'run' in purpose.get_text().lower():
                is_running_shoe = True

        if is_running_shoe: shoes_array.append(shoe)


shoes = []
driver = webdriver.Chrome()
page = get_page_html(HOKA_URL, driver)
parse_page(page, shoes)
write_output('hoka', shoes)
