def filter_tokens(tokens):

    result = []

    for token in tokens:

        liquidity = token.get("liquidity", 0)

        volume = token.get("volume24h", 0)

        if liquidity < 50000:
            continue

        if volume < 100000:
            continue

        result.append(token)

    return result
