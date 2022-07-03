from scraper import Scraper

BROOKS_URL = "https://www.brooksrunning.com/en_us/all-mens-running-shoes/"


class BrooksScraper(Scraper):
    def get_shoe_name(self, card, shoe):
        shoe_name = card.find("h2").get_text().strip()
        shoe["name"] = shoe_name

    def get_page_url(self, card, shoe):
        shoe_page_url = card.find("a")["href"]
        shoe["page_url"] = f"https://brooksrunning.com{shoe_page_url}"

    def get_img_url(self, card, shoe):
        img_urls = card.find_all("img")
        for url in img_urls:
            url_src = url["src"]
            if "http" in url_src and "award" not in url_src:
                shoe["img_url"] = url_src
                break


scraper = BrooksScraper(
    brand_name="brooks",
    url=BROOKS_URL,
    card_class="m-product-tile",
    name_class="",
    price_class="pricing__sale",
    price_idx=-1,
).scrape()
