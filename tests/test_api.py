import requests

url = "http://127.0.0.1:8000/api"
headers = {"x-api-key": "valid-key"}

for i in range(10):
    r = requests.get(url, headers=headers)
    print(i+1, r.json())
