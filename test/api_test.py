import pytest
import requests
from decimal import *
import json
from datetime import datetime

url = "http://127.0.0.1:5000/rate"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

# load input data from a file
def load_input(fileName):
    f = open("rate.json")
    payload = f.read()
    return payload

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_status_code_equals_200(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    assert response.status_code == 200

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_content_type_equals_json(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload)
    assert response.headers["Content-Type"] == "application/json"

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_input_format(json_file_name):
    payload = load_input(json_file_name)
    payload = json.loads(payload)
    assert list(payload.keys()) == ['rate','cdr']

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_input_rate_format(json_file_name):
    payload = load_input(json_file_name)
    payload = json.loads(payload)
    assert list(payload['rate'].keys()) == ['energy','time','transaction']

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_input_cdr_format(json_file_name):
    payload = load_input(json_file_name)
    payload = json.loads(payload)
    assert list(payload['cdr'].keys()) == ['meterStart','timestampStart','meterStop','timestampStop']

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_timestamp_format(json_file_name):
    payload = load_input(json_file_name)
    payload = json.loads(payload)
    assert datetime.strptime(payload['cdr']['timestampStart'], "%Y-%m-%dT%H:%M:%SZ") and datetime.strptime(payload['cdr']['timestampStop'], "%Y-%m-%dT%H:%M:%SZ")


@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_output_format(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    response_body = response.json()
    assert list(response_body.keys()) == ['overall','components']

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_overall_format(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    response_body = response.json()
    assert type(response_body['overall']) == float or type(response_body['overall']) == int

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_components_format(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    response_body = response.json()
    assert type(response_body['components']) == dict and list(response_body['components'].keys()) == ['energy','time','transaction']

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_components_value_format(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    response_body = response.json()
    assert ((type(response_body['components']['energy']) == float or type(response_body['components']['energy']) == int) and
     (type(response_body['components']['time']) == float or type(response_body['components']['time']) == int) and
      (type(response_body['components']['transaction']) == float or type(response_body['components']['transaction']) == int))


@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_overall_decimal_place(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    response_body = response.json()
    assert Decimal(str(response_body['overall'])).as_tuple().exponent >= -2

@pytest.mark.parametrize("json_file_name",['rate.json'])
def test_post_check_components_decimal_place(json_file_name):
    payload = load_input(json_file_name)
    response = requests.request("POST", url, data=payload, headers=headers)
    response_body = response.json()
    assert (Decimal(str(response_body['components']['energy'])).as_tuple().exponent >= -3 and
     Decimal(str(response_body['components']['time'])).as_tuple().exponent >= -3 and
     Decimal(str(response_body['components']['transaction'])).as_tuple().exponent >= -3)