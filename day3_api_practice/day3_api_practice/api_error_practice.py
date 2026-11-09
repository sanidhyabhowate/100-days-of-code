import requests

url = "https://jsonplaceholder.typicode.com/posts/999999"

try:
    response = requests.get(url,timeout=10)
    response.raise_for_status()

    data = response.json()
    print(data)

except requests.exceptions.HTTPError:
    print("HTTP Error: Resource not found or request failed.")

except requests.exceptions.Timeout:
    print("Error: Request timesout.")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed.")