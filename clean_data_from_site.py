from bs4 import BeautifulSoup
import requests
import string

roman_to_arabic = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9', 'X': '10'}
page_url = 'https://wydawnictwowarstwy.pl/strona-glowna/174-my-kobiety-z-teatru-kalambur-herstorie-9788367186070.html'
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

punctuation_title = soup.find(class_='h1 product-detail-name').get_text()
title = punctuation_title.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")
table = soup.find('dt')
cover = soup.find_all('dd')[1].get_text().lower()
punctuation_edition_info = soup.find_all('dd')[3].get_text()
edition_info = punctuation_edition_info.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ").split(" ")
for edition_data in edition_info:
    if edition_data in roman_to_arabic:
        edition = roman_to_arabic[edition_data]
year = ""
for edition_data in edition_info:
    if edition_data.isdigit():
        year += edition_data
        year = int(year)
punctuation_isbn = soup.find_all('dd')[4].get_text()
isbn = punctuation_isbn.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")

print(f"title: {title}")
print(f"year: {year}")
print(f"edition: {edition}")
print(f"isbn: {isbn}")
print(f"cover: {cover}")



