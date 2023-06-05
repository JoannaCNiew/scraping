import json
import requests
import string


next_page = 'https://data.bn.org.pl/api/institutions/bibs.json?kind=ksi%C4%85%C5%BCka&publisher=Wroc%C5%82awskie+Wydawnictwo+Warstwy&sinceId=3904564"'
while next_page != "":
    response = requests.get(next_page)
    content = response.content
    data = json.loads(content)
    for item in data['bibs']:
        punctuation_title = item['title']
        title = punctuation_title.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")
        isbn = item['isbnIssn']
        year = item['publicationYear']
        try:
            punctuation_cover = item['marc']['fields'][5]['020']['subfields'][1]['q']
            cover = punctuation_cover.translate(str.maketrans('', '', string.punctuation)).replace("  ", " ")[7:]
        except:
            cover = ""
        print(title)
        print(year)
        print(isbn)
        print(cover)
    next_page = data['nextPage']



