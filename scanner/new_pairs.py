import requests

DEX_URL = "https://api.dexscreener.com/token-profiles/latest/v1"


def get_new_pairs():

    try:

        response = requests.get(
            DEX_URL,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data

    except Exception as e:

        print(e)

        return []
