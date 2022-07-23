#!/usr/bin/bash

scrapers=('adidas_scraper.py' 'brooks_scraper.py' 'hoka_scraper.py' 'new_balance_scraper.py' 'nike_scraper.py' 'saucony_scraper.py')

for scraper in ${scrapers[@]}; do
  python $scraper
done

python merge.py
