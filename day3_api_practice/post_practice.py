import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My Python Journey",
    "body": "I am completing Python fundamentals.",
    "userId": 5
}

response = requests.post(url, json=new_post, timeout=10)

response.raise_for_status()

print(response.status_code)

data = response.json()

print(data["title"])
print(data["body"])
print(data["userId"])