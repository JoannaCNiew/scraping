from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import string

from scrap_warstwy.models import Publisher, Book
from scrap_warstwy.clean_links_all_sites import urls_warstwy

class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        for link in urls_warstwy:
            roman_to_arabic = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5',
                               'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9', 'X': '10'}
            result = requests.get(link)
            content = result.text
            soup = BeautifulSoup(content, 'html.parser')
            try:
                punctuation_title = soup.find(class_='h1 product-detail-name').get_text()
                title = punctuation_title.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")
                table = soup.find('dt')
                cover = soup.find_all('dd')[1].get_text().lower()
                punctuation_edition_info = soup.find_all('dd')[3].get_text()
                edition_info = punctuation_edition_info.translate(str.maketrans('', '', string.punctuation)).replace(
                    "  ", " ").split(" ")
                for edition_data in edition_info:
                    if edition_data in roman_to_arabic:
                        edition = roman_to_arabic[edition_data]
                year = ""
                for edition_data in edition_info:
                    if edition_data.isdigit():
                        year += edition_data
                punctuation_isbn = soup.find_all('dd')[4].get_text()
                isbn = punctuation_isbn.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")
            except:
                pass

            if not Book.objects.filter(isbn=isbn).exists():
                Book.objects.create(
                    title=title,
                    year=year,
                    edition=edition,
                    isbn=isbn,
                    cover=cover,
                    publisher=Publisher.objects.get(name='Wrocławskie Wydawnictwo Warstwy')
                )