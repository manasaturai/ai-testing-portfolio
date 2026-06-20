import requests

def api_return_data(url:str)->dict:
 response = requests.get(url)
 response.raise_for_status()
 return response.json()
url="https://api.github.com"

data = api_return_data(url)
print(data)