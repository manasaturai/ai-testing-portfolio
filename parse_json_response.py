import requests
response = requests.get("https://api.github.com")
data = (response.json())
print(f"GitHub API Version:{data['current_user_url']}")