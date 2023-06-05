from bs4 import BeautifulSoup
import requests
from clean_links_all_sites import urls_warstwy

for link in urls_warstwy:
    result = requests.get(link)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    info_title = soup.find(class_='h1 product-detail-name').get_text()
    try:
        table = soup.find('dt')
        cover = soup.find_all('dd')[1].get_text()
        # edition = soup.find_all('dd')[3].get_text()
        isbn = soup.find_all('dd')[4].get_text()
    except:
        pass

    print(f"title: {info_title}")
    print(f"cover: {cover}")
    # print(f"edition: {edition}")
    print(f"isbn: {isbn}")




