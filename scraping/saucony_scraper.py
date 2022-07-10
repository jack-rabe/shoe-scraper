# NOTE: does not get sale price of shoe
# (no shoes were on sale when this was written)
import time
from selenium.webdriver.common.by import By
from scraper import Scraper

SAUCONY_URL = "https://www.saucony.com/en/mens-running/"


class SauconyScraper(Scraper):
    def get_shoe_name(self, card, shoe):
        shoe_name = card.find(class_="name-link").get_text()
        shoe["name"] = shoe_name.replace("Men's", "").strip()

    def get_price(self, card, shoe):
        price = card.find(class_="product-sales-price").get_text()
        price_str = price.replace("Sale Price", "").replace("$", "").strip()
        try:
            price = int(price_str)
        except Exception as e:
            price = float(price_str)
        shoe["price"] = price

    def get_img_url(self, card, shoe):
        img_urls = card.find_all("img")
        img_url = img_urls[-1]["src"]
        shoe["img_url"] = img_url

    # load more button appears at bottom of page if lots of shoes
    def scroll_to_bottom(self):
        driver = self.driver

        height = driver.execute_script("return document.body.scrollHeight")
        position = 700
        while position < height:
            driver.execute_script(f"window.scrollTo(0, { position });")
            time.sleep(3)
            height = driver.execute_script("return document.body.scrollHeight")
            position += 700
            # remove the pop up ads
            try:
                popup = driver.find_element(By.CLASS_NAME, "bx-close-xsvg")
                popup.click()
                pass
            except Exception as e:
                pass
            # check to see if more shoes can be loaded
            try:
                more_btn = driver.find_element(By.CLASS_NAME, "load-more-cta")
                more_btn.click()
            except Exception as e:
                pass


scraper = SauconyScraper(
    brand_name="saucony",
    url=SAUCONY_URL,
    card_class="product-tile",
    name_class=None,
    price_class="product-sales-price",
    price_idx=None,
).scrape()
