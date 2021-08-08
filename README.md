# CSMS-for-HTB
Simple overview of charging station management system Coding Challenge.

## Description
A  CSMS  (charging  station  management  system)  such  as  be.ENERGISED  is  used  to  manage  charging  stations,  charging 
processes and customers (so-called eDrivers) amongst other things.
One of the most important functionalities of such a CSMS is to calculate a price to a particular charging process so that 
the  eDriver  can  be  invoiced  for  the  consumed  services.  Establishing  a  price  for  a  charging  process  is  usually  done  by 
applying a rate to the CDR (charge detail record) of the corresponding charging process

## Getting Started
### Dependencies
* This project created by Flask, python, html, javascript

### Installing
* for install requiremets run this in terminal
pip install -r requirements.txt

### Executing program
* for activate env in windows you can run this in terminal
env\Scripts\activate 

* running the app run this in terminal
python .\api.py 

### Project section
* api.py -> rate post api
* app.py -> all functions for calculating the result based on input
* CSMS.html -> simple html page for testing api with ui
* .\test\rate.json -> input value for running the api
* .\test\run.py -> running test api with python
* .\test\api_test.pt -> simple unit tests with pytest for Rate api

## Help
* if you wanted to running unittest run this in terminal when the api is running
pytest .\unittest.py

* The api http post request is like below 
```
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
```

* If you want to test it with cURL you can use like this example:
```
curl -X POST \
  http://127.0.0.1:5000/rate \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "rate": { "energy": 0.3, "time": 2, "transaction": 1 },
  "cdr": { "meterStart": 1204307, "timestampStart": "2021-04-05T10:04:00Z", "meterStop": 1215230, "timestampStop": 
"2021-04-05T11:27:00Z" }
}'

```

* If want to test it with Python you can use like this example
python .\test\run.py

* If want to test it with UI you can use like this example
open http://127.0.0.1:5000/rate in your browser
fill all inputs
click on Apply Button
you can see the result at the end of the page


## Author
[Shamim Sanisales](https://shsanisales.ir)

## Acknowledgments
* This code is written for HTB's code challenge by Shamim
