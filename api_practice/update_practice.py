import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_post = {
    "id": 1,
    "title": "Updated Python Journey.",
    "body": "I am learning HTTP methods.",
    "userId": 5
}

changes = {
    "title": "Learning AI and Web Development."
}

response = requests.put(url, json=updated_post, timeout=10)
response.raise_for_status()

data = response.json()

print(response.status_code)
print(data["title"])
print(data["body"])

patch_response = requests.patch(url, json=changes,timeout=10)
patch_response.raise_for_status()

data = patch_response.json()

print(patch_response.status_code)
print(data["title"])
