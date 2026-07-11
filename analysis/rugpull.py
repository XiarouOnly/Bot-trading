"""
Rugpull Risk Engine v1
"""

def check(pair):

    risk = 0

    reasons = []

    liquidity = pair["liquidity"]["usd"]

    fdv = pair.get("fdv", 0)

    buys = pair["txns"]["h24"]["buys"]

    sells = pair["txns"]["h24"]["sells"]

    change = pair["priceChange"]["h24"]

    # Liquidity

    if liquidity < 10000:

        risk += 35

        reasons.append("Liquidity sangat kecil")

    elif liquidity < 50000:

        risk += 20

        reasons.append("Liquidity rendah")

    # FDV

    if fdv > 100000000:

        risk += 15

        reasons.append("FDV terlalu tinggi")

    # Buy Sell

    if sells > buys * 2:

        risk += 20

        reasons.append("Tekanan jual tinggi")

    # Pump berlebihan

    if change > 500:

        risk += 15

        reasons.append("Pump terlalu tinggi")

    if risk <= 20:

        level = "LOW"

    elif risk <= 40:

        level = "MEDIUM"

    else:

        level = "HIGH"

    return {

        "risk_score": risk,

        "risk_level": level,

        "reasons": reasons

      }
