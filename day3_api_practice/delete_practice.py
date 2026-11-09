import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url, timeout=10)
response.raise_for_status

print(response.status_code)
print(response.json())