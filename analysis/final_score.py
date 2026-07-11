"""
Final AI Decision Engine
"""

def build(score_data, momentum_data, rugpull_data):

    total = 0

    total += score_data["score"]

    total += int(momentum_data["score"] / 4)

    total -= rugpull_data["risk_score"]

    if total > 100:
        total = 100

    if total < 0:
        total = 0

    if total >= 90:

        signal = "🔥 STRONG BUY"

    elif total >= 80:

        signal = "🟢 BUY"

    elif total >= 70:

        signal = "🟡 WATCH"

    elif total >= 60:

        signal = "🟠 WAIT"

    else:

        signal = "🔴 SKIP"

    confidence = min(99, max(35, total))

    return {

        "ai_score": total,

        "signal": signal,

        "confidence": confidence

    }
