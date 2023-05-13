import json
import requests

url = 'https://api.apilayer.com/fixer/latest?base=EUR'


def get_rates(api_key):
    """
    send a get requests to the fixer.io api and get live rates
    :return: request.Response instance
    """
    headers={
        'apikey' : api_key,
    }
    # Send HTTP Request
    response = requests.request("GET", url, headers=headers)
    # Check the status
    status_code = str(response.status_code)
    if status_code.startswith('2'):
        print(response.text)
        return json.loads(response.text)
        
    return None
