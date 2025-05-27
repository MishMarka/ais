import requests

url = "http://localhost:5000/crawl"
data = {
    "url": "https://facebook.com",
    "depth": 1
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
