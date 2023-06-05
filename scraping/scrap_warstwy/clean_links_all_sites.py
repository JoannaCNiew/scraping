from bs4 import BeautifulSoup
import requests

page = 1
urls_warstwy = []
while page != 13:
   url = f"https://wydawnictwowarstwy.pl/88-ksiegarnia?page={page}"
   req = requests.get(url)
   soup = BeautifulSoup(req.content, "lxml")
   for link in soup.find_all('a', class_='thumbnail product-thumbnail'):
      urls_warstwy.append(link.get('href'))
   page = page + 1
print(urls_warstwy)
