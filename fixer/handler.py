import json
import requests

url = 'https://api.apilayer.com/fixer/latest?base=EUR'


def get_rates(API_KEY):
    """
    send a get requests to the fixer.io api and get live rates
    :return: request.Response instance
    """
    headers = {
        'api_key': API_KEY,
    }
    # Send HTTP Request
    response = requests.request("GET", url, headers=headers)
    # Check the status
    status_code = str(response.status_code)
    if status_code.startswith('2'):
        return json.loads(response.text)
    return None
