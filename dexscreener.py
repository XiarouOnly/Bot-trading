import requests

BASE_URL = "https://api.dexscreener.com/latest/dex"


def get_token(address):

    url = f"{BASE_URL}/tokens/{address}"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        if "pairs" not in data:
            return None

        if len(data["pairs"]) == 0:
            return None

        return data["pairs"][0]

    except Exception as e:

        print(e)

        return None
