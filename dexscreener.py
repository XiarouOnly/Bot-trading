import requests

BASE_URL = "https://api.dexscreener.com/latest/dex"


def get_token(address):
    url = f"{BASE_URL}/tokens/{address}"

    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": "XiarouScannerAI/1.0"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        pairs = data.get("pairs", [])

        if not pairs:
            return None

        pairs.sort(
            key=lambda x: float(
                x.get("liquidity", {}).get("usd", 0)
            ),
            reverse=True
        )

        return pairs[0]

    except requests.exceptions.RequestException as e:
        print(f"DexScreener Error: {e}")
        return None
