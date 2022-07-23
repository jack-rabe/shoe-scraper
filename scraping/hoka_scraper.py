from scraper import Scraper

HOKA_URL = "https://www.hoka.com/en/us/mens-view-all/?sz=10000"


class HokaScraper(Scraper):
    def get_shoe_name(self, card, shoe):
        name_div = card.find(class_="tile-product-name")
        shoe_name = name_div.find("a").get_text()
        shoe_name = shoe_name.replace("Men's", "").replace("All Gender", "")
        shoe["name"] = shoe_name.strip()

    def is_running_shoe(self, card):
        is_running_shoe = False
        for purpose in card.find_all(class_="best-for__surface"):
            if "run" in purpose.get_text().lower():
                is_running_shoe = True
        return is_running_shoe

    def get_page_url(self, card, shoe):
        name_div = card.find(class_="tile-product-name")
        shoe_page_url = f"https://hoka.com{name_div.find('a')['href']}"
        shoe["page_url"] = shoe_page_url


scraper = HokaScraper(
    brand_name="hoka",
    url=HOKA_URL,
    card_class="product",
    name_class="",
    price_class="sales",
    price_idx=0,
).scrape()
