from bs4 import BeautifulSoup
import requests

page_url = 'https://wydawnictwowarstwy.pl/88-ksiegarnia'
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

# kod Jerzego, który działa
# next_book = soup.find_all('a', href=True, class_='thumbnail product-thumbnail')
# print(next_book[0].get('href'))

# box = soup.find('article', class_='thumbnail-container')
# links = [link['href'] for link in box.find_all('a', href=True)]
# print(links)
# for link in links:
#     result = requests.get(f'{root}/{link}')
#     content = result.text
#     soup = BeautifulSoup(content, 'lxml')

# next_book = soup.find_all('a', href=True, class_='thumbnail product-thumbnail')
a_href=soup.find("a",{"class":"thumbnail product-thumbnail"})
for link in a_href('a'):
    link.get('href')
    print(link)