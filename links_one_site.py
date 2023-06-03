from bs4 import BeautifulSoup
import requests
url = "https://wydawnictwowarstwy.pl/88-ksiegarnia"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
for link in soup.find_all('a', class_='thumbnail product-thumbnail'):
   print(link.get('href'))