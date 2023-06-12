import json
import requests
import string

response = requests.get('https://data.bn.org.pl/api/institutions/bibs.json?kind=ksi%C4%85%C5%BCka&publisher=Wroc%C5%82awskie%20Wydawnictwo%20Warstwy')
content = response.content

data = json.loads(content)
for item in data['bibs']:
    year = item['publicationYear']
    marc_fields_list = item.get('marc').get('fields')
    isbn = ""
    punctuation_title = ""
    punctuation_cover = ""

    for marc_field_dict in marc_fields_list:
        if '020' in marc_field_dict:
            subfields_list = marc_field_dict.get('020').get('subfields')
            for marc_subfield_dict in subfields_list:
                if 'a' in marc_subfield_dict:
                    isbn += marc_subfield_dict.get('a')
                if 'q' in marc_subfield_dict:
                    punctuation_cover += marc_subfield_dict.get('q')
                cover = punctuation_cover.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")
        if '245' in marc_field_dict:
            subfields_list = marc_field_dict.get('245').get('subfields')
            title_to_join = []
            for marc_subfield_dict in subfields_list:
                if 'a' in marc_subfield_dict:
                    punctuation_title += marc_subfield_dict.get('a')
                if 'b' in marc_subfield_dict:
                    punctuation_title += marc_subfield_dict.get('b')
            title = punctuation_title.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")

            print(title)
            print(year)
            print(isbn)
            print(cover)