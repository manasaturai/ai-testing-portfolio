import requests

def api_return_data(url:str)->dict:
 response = requests.get(url)
 response.raise_for_status()
 return response.json()
url="https://api.github.com/invalid"

try:
   data = api_return_data(url)
   print(data)
except requests.HTTPError as e:
   print(f"API error:{e}")