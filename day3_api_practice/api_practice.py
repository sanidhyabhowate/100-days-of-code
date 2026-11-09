import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()

print(data["id"])
print(data["title"])
print(data["completed"])