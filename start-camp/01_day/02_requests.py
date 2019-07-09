import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

response = requests.get(url)  #requests.get html파일 요청을 보내받는것.

print(response)
print(response.status_code)    #상태코드 

html = response.text    # text는 파일 안에 정보를 받아오는 함수 

soup = BeautifulSoup(html, 'html.parser')    #bs4모듈의 beautufulsoup을 통해 받아오는 정보를 변환
kospi = soup.select_one('#KOSPI_now').text  #select는 특정 내용을 뽑아주는 함수(여러개) select_one은 특정내용 단하나를 뽑아주는 함수 
                                        # id로 접근할때는 #id로 접근 

print(kospi)
