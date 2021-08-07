import requests

url = "http://127.0.0.1:5000/rate"

f = open("rate.json")
payload = f.read()

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
