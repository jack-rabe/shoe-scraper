import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, brand_name, url, card_class, name_class, price_class, price_idx):
        self.brand_name = brand_name
        self.url = url
        self.card_class = card_class
        self.name_class = name_class
        self.price_class = price_class
        self.price_idx = price_idx

        self.shoes = []

        self.driver = webdriver.Chrome()

    def get_page_html(self):
        self.setup_driver()
        self.scroll_to_bottom()

        time.sleep(3)
        page = self.driver.page_source
        self.driver.quit()

        parsed_page = BeautifulSoup(page, "html.parser")
        return parsed_page

    def setup_driver(self):
        self.driver.get(self.url)
        self.driver.fullscreen_window()

    def scroll_to_bottom(self):
        driver = self.driver

        height = driver.execute_script("return document.body.scrollHeight")
        position = 700
        while position < height:
            driver.execute_script(f"window.scrollTo(0, { position });")
            time.sleep(3)
            height = driver.execute_script("return document.body.scrollHeight")
            position += 700

    def get_cards(self, html):
        return html.find_all(class_=self.card_class)

    def get_shoe_name(self, card, shoe):
        shoe_name = card.find(class_=self.name_class).get_text()
        shoe["name"] = shoe_name

    def get_img_url(self, card, shoe):
        img_url = card.find("img")["src"]
        shoe["img_url"] = img_url

    def get_page_url(self, card, shoe):
        shoe_page_url = card.find("a")["href"]
        shoe["page_url"] = shoe_page_url

    # sometimes there are multiple prices during a sale (so specify an index)
    def get_price(self, card, shoe):
        price = card.find_all(class_=self.price_class)
        price_str = price[self.price_idx].get_text().replace("$", "")
        try:
            price = int(price_str)
        except:
            price = float(price_str)
        shoe["price"] = price

    def is_running_shoe(self, _card):
        return True

    def parse_page(self, html):
        cards = self.get_cards(html)

        for card in cards:
            shoe = {"brand": self.brand_name}
            # populate shoe with link, img, name, and price
            self.get_shoe_name(card, shoe)
            self.get_img_url(card, shoe)
            self.get_page_url(card, shoe)
            self.get_price(
                card,
                shoe,
            )
            # append final shoe to list
            if self.is_running_shoe(card):
                self.shoes.append(shoe)

    def write_output(self):
        brand_name = self.brand_name
        shoes_array = self.shoes

        modified_name = brand_name.replace(" ", "_")
        with open(f"../data/{modified_name}_shoes.json", "w") as f:
            output = {
                "brand": brand_name,
                "count": len(shoes_array),
                "shoes": shoes_array,
            }
            json.dump(output, f, indent=4)

    def scrape(self):
        page = self.get_page_html()
        self.parse_page(page)
        self.write_output()
