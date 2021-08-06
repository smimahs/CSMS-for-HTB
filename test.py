import requests

url = "http://127.0.0.1:5000/price"

payload = "{\r\n  \"rate\": { \"energy\": 0.3, \"time\": 2, \"transaction\": 1 },\r\n  \"cdr\": { \"meterStart\": 1204307, \"timestampStart\": \"2021-04-05T10:04:00Z\", \"meterStop\": 1215230, \"timestampStop\": \r\n\"2021-04-05T11:27:00Z\" }\r\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "277e4d26-d54d-43ea-02c7-4f266c1259d2"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)