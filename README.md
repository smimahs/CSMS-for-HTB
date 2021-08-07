# CSMS-for-HTB
charging station management system Coding Challenge

# activate env
env\Scripts\activate 

# for install requiremets
pip install -r requirements.txt

# running unittest:
pytest .\unittest.py


The api is like this:
POST /rate HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Cache-Control: no-cache

{
  "rate": { "energy": energyFee, "time": timeFee, "transaction": transactionFee },
  "cdr": { "meterStart": meterStart, "timestampStart": timestampStart (according to ISO 8601), "meterStop": meterStop, "timestampStop":
  timestampStop (according to ISO 8601) }
}

If you want to test it with cURL you can use like this example:
curl -X POST \
  http://127.0.0.1:5000/rate \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "rate": { "energy": 0.3, "time": 2, "transaction": 1 },
  "cdr": { "meterStart": 1204307, "timestampStart": "2021-04-05T10:04:00Z", "meterStop": 1215230, "timestampStop": 
"2021-04-05T11:27:00Z" }
}'