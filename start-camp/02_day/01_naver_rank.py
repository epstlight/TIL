import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
lists = soup.select('.ah_l .ah_item .ah_a .ah_k')[:20]

for i in lists :
    print(i.text)


