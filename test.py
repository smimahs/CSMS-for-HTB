import requests

url = "http://127.0.0.1:5000/charging"

payload = "{\n  \"rate\": { \"energy\": 0.3, \"time\": 2, \"transaction\": 1 },\n  \"cdr\": { \"meterStart\": 1204307, \"timestampStart\": \"2021-04-05T10:04:00Z\", \"meterStop\": 1215230, \"timestampStop\": \n\"2021-04-05T11:27:00Z\" }\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "da3bcbf9-cfdc-c58f-54e1-32ed33093790"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)