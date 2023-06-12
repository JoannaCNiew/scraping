from django.core.management.base import BaseCommand
import json
from bs4 import BeautifulSoup
import requests
import string

from scrap_warstwy.models import Publisher, Deposit


class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        next_page = 'https://data.bn.org.pl/api/institutions/bibs.json?kind=ksi%C4%85%C5%BCka&publisher=Wroc%C5%82awskie+Wydawnictwo+Warstwy&sinceId=3904564"'
        while next_page != "":
            response = requests.get(next_page)
            content = response.content
            data = json.loads(content)
            for item in data['bibs']:
                roman_to_arabic = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5',
                                   'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9', 'X': '10'}
                year = item['publicationYear']
                marc_fields_list = item.get('marc').get('fields')
                isbn = ""
                punctuation_title = ""
                punctuation_cover = ""
                punctuation_edition_info = ""

                for marc_field_dict in marc_fields_list:
                    if '020' in marc_field_dict:
                        subfields_list = marc_field_dict.get('020').get('subfields')
                        for marc_subfield_dict in subfields_list:
                            if 'a' in marc_subfield_dict:
                                isbn += marc_subfield_dict.get('a')
                            if 'q' in marc_subfield_dict:
                                punctuation_cover += marc_subfield_dict.get('q')
                            cover = punctuation_cover.translate(str.maketrans('', '', string.punctuation)).replace("  ",
                                                                                                                   " ")
                            cover = cover.replace("oprawa ", "")
                    if '245' in marc_field_dict:
                        subfields_list = marc_field_dict.get('245').get('subfields')
                        title_to_join = []
                        for marc_subfield_dict in subfields_list:
                            if 'a' in marc_subfield_dict:
                                punctuation_title += marc_subfield_dict.get('a')
                            if 'b' in marc_subfield_dict:
                                punctuation_title += marc_subfield_dict.get('b')
                        title = punctuation_title.translate(str.maketrans('', '', string.punctuation)).replace("  ",
                                                                                                               " ")
                    if '250' in marc_field_dict:
                        subfields_list = marc_field_dict.get('250').get('subfields')
                        for marc_subfield_dict in subfields_list:
                            if 'a' in marc_subfield_dict:
                                punctuation_edition_info += marc_subfield_dict.get('a')
                                edition_info = punctuation_edition_info.translate(
                                    str.maketrans('', '', string.punctuation)).replace(
                                    "  ", " ").split(" ")
                                for edition_data in edition_info:
                                    if edition_data in roman_to_arabic:
                                        edition = roman_to_arabic[edition_data]

                                        if not Deposit.objects.filter(isbn=isbn).exists():
                                            Deposit.objects.create(
                                                title=title,
                                                year=year,
                                                edition=edition,
                                                isbn=isbn,
                                                cover=cover,
                                            )

            next_page = data['nextPage']