import requests
from bs4 import BeautifulSoup

url = 'https://www.bithumb.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

coins = soup.select('.coin_list tr') # " " 안에 전부다 > 안에 가장가까운 하나 

import csv

with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f :
    csv_writer = csv.writer(f)

    for coin in coins :
        coin_name = coin.select_one(f'td:nth-child(1) > p > a > strong').text.strip().replace('NEW', '')
        coin_price = coin.select_one(f'td:nth-child(2) > strong').text
        data = (coin_name, coin_price)
        csv_writer.writerow(data)
    




        
