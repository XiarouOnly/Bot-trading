"""
Momentum Analysis Engine
"""

def analyze(pair):

    score = 0

    reasons = []

    change5 = pair["priceChange"].get("m5", 0)
    change1h = pair["priceChange"].get("h1", 0)
    change24 = pair["priceChange"].get("h24", 0)

    volume = pair["volume"]["h24"]

    buys = pair["txns"]["h24"]["buys"]
    sells = pair["txns"]["h24"]["sells"]

    # Volume

    if volume > 1000000:
        score += 30
        reasons.append("Volume sangat tinggi")

    elif volume > 250000:
        score += 20
        reasons.append("Volume bagus")

    # Momentum

    if change5 > 5:
        score += 15
        reasons.append("Momentum 5m positif")

    if change1h > 10:
        score += 20
        reasons.append("Momentum 1h kuat")

    if change24 > 25:
        score += 15
        reasons.append("Trend 24h bullish")

    # Buy Sell

    if buys > sells:
        score += 20
        reasons.append("Buyer mendominasi")

    return {
        "score": score,
        "reasons": reasons
  }
