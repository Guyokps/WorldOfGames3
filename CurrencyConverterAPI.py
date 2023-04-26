import requests
import json


def ils_to_usd_converter(amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount={amount}"

    payload = {}
    headers = {
        "apikey": "8V5SQDJfUap0WgSOhpA1gc85bT0iHhp3"
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    data_dict = json.loads(result)
    result = data_dict['result']

    return result
