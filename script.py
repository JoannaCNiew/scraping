from bs4 import BeautifulSoup
import requests

page_url = 'https://wydawnictwowarstwy.pl/strona-glowna/171-nie-boli-9788367186933.html'
page = requests.get(page_url)

# print(soup.prettify())

info_title = soup.find(class_='h1 product-detail-name').get_text()

soup = BeautifulSoup(page.content, 'html.parser')
# info_book = soup.find(id='product-details').get_text()
#
print(f"title: {info_title}")
# print(info_book)

# table_rows = soup.find_all('dt')
# for dt in table_rows:
#     dd = dt.find_all('dd')
#     row = [i.get_text for i in dd]
#     print(row)

table = soup.find_all('dt')
for dt in table:
    cover = soup.find_all('dd')[1].get_text()
    edition = soup.find_all('dd')[3].get_text()
    isbn = soup.find_all('dd')[4].get_text()
print(f"cover: {cover}")
print(f"edition: {edition}")
print(f"isbn: {isbn}")