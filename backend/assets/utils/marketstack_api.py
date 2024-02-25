import requests

MARKETSTACK_API_KEY = '8d0ccf8df53f6ec87aa0eeabec9a9610'

def fetch_bulk_eod_data(symbols):
  endpoint = "http://api.marketstack.com/v1/eod/latest"
  test_endpoint = "http://localhost:5000/eod_data"
  params = {
    "access_key": MARKETSTACK_API_KEY,
    "symbols": ','.join(symbols)
  }
  try:
    # response = requests.get(endpoint, params=params)
    response = requests.get(test_endpoint)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    data = response.json()
    return data['data']
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Marketstack API: {e}")
    return {}
