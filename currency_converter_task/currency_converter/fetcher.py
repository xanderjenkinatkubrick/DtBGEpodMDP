import sys
import requests

def fetch_exchange_rate(base: str, target: str) -> float:
    ACCESS_KEY = '4e62ad6d7f0b01fa8a777ed4d0fc324c' # Should the Access Key be stored this way?
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={ACCESS_KEY}&symbols={base},{target}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        base_rate = data["rates"].get(base)
        target_rate = data["rates"].get(target)
        return target_rate , base_rate
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Invalid target currency '{target}' or no rate available.")
        sys.exit(1)