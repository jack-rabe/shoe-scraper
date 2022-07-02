from scraper import Scraper

NIKE_URL = "https://www.nike.com/w/mens-running-shoes-37v7jznik1zy7ok"


class NikeScraper(Scraper):
    def get_shoe_name(self, card, shoe):
        shoe_name = card.find(class_="product-card__link-overlay").get_text()
        shoe["name"] = shoe_name.replace("Nike", "").strip()


scraper = NikeScraper(
    brand_name="nike",
    url=NIKE_URL,
    card_class="product-card__body",
    name_class="product-card__link-overlay",
    price_class="product-price",
    price_idx=0,
).scrape()
