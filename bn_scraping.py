from pymarc import MARCReader

def get_data(self, api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        print("sucessfully fetched the data")
    self.formatted_print(response.json())
else:
print(f"Hello person, there's a {response.status_code} error with your request")