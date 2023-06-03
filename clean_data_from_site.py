from bs4 import BeautifulSoup
import requests


page_url = 'https://wydawnictwowarstwy.pl/strona-glowna/174-my-kobiety-z-teatru-kalambur-herstorie-9788367186070.html'
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

info_title = soup.find(class_='h1 product-detail-name').get_text()
table = soup.find('dt')
cover = soup.find_all('dd')[1].get_text()
edition = soup.find_all('dd')[3].get_text()
isbn = soup.find_all('dd')[4].get_text()

print(f"title: {info_title}")
print(f"cover: {cover}")
print(f"edition: {edition}")
print(f"isbn: {isbn}")

