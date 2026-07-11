def calculate(pair):

    score = 0

    reasons = []

    liquidity = pair["liquidity"]["usd"]

    volume = pair["volume"]["h24"]

    buys = pair["txns"]["h24"]["buys"]

    sells = pair["txns"]["h24"]["sells"]

    fdv = pair.get("fdv", 0)

    change = pair["priceChange"]["h24"]

    if liquidity > 100000:

        score += 20

        reasons.append("Liquidity kuat")

    if volume > 250000:

        score += 20

        reasons.append("Volume tinggi")

    if buys > sells:

        score += 15

        reasons.append("Buyer dominan")

    if fdv < 5000000:

        score += 15

        reasons.append("FDV sehat")

    if change > 15:

        score += 15

        reasons.append("Momentum naik")

    if liquidity > 500000:

        score += 15

        reasons.append("Likuiditas sangat tinggi")

    return {

        "score": score,

        "reasons": reasons,

        "liquidity": liquidity,

        "volume": volume,

        "fdv": fdv,

        "change": change

    }
