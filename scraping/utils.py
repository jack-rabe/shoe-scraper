import time
import json
from bs4 import BeautifulSoup

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


def write_output(brand_name, shoes_array):
    modified_name = brand_name.replace(' ', '_');
    with open(f'../data/{modified_name}_shoes.json', 'w') as f:
        output = {
                'brand': brand_name,
                'count': len(shoes_array),
                'shoes': shoes_array
                }
        json.dump(output, f, indent=4)
